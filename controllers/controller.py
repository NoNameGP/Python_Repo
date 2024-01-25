from flask_restful import Resource
from flask import request
from models.model import db
from flask_login import logout_user, login_required
from services.service import *
from dto.dto import *
from controllers.BaseResponse import BaseResponse
from flask_socketio import SocketIO, emit
import cv2
import math
from ultralytics import YOLO


class UserResource(Resource):

    def post(self):
        data = request.get_json()

        user_data = UserDTO(**data)
        user_service = UserService()
        user, response = UserService.register_user(user_service, user_data)

        if not response['success']:
            return response, 400

        db.session.add(user)
        db.session.commit()

        login_user(user)

        return BaseResponse(True, '회원가입과 로그인 성공').to_response()


class Session(Resource):
    def post(self):
        json_data = request.get_json()

        user_service = UserService()
        UserService.login_user(user_service, UserDTO(**json_data))
        return BaseResponse(True, "로그인 성공").to_response()

    @login_required
    def patch(self):
        logout_user()
        return BaseResponse(True, '로그 아웃 성공').to_response()


class RouteResource(Resource):
    def post(self):
        data = request.get_json()

        routeReq = RouteDTO(**data)

        route_service = RouteService()
        route = route_service.save_route(routeReq)
        db.session.add(route)
        db.session.commit()

        pass_point_controller = PassPointController()
        pass_point_controller.save_pass_points(routeReq.pass_points, route)

        object_controller = ObjectController()
        object_controller.save_object(routeReq.objects, route)

        db.session.commit()

        return BaseResponse(True, '경로 추가 성공').to_response()

    def get(self, departure, arrival):
        route_service = RouteService()

        best_route = route_service.find_route(departure, arrival).to_dict()
        return BaseResponse(True, '장애물이 적은 경로 조회 성공', data=best_route).to_response()


class MarkResourece(Resource):
    def post(self):
        data = request.get_json()

        mark_data = MarkDTO(**data)

        mark_service = MarkService()

        mark = mark_service.save_object(mark_data)

        db.session.add(mark)
        db.session.commit()

        return BaseResponse(True, '즐겨찾기 추가 완료').to_response()

    def get(self, email):
        mark_service = MarkService()
        mark = mark_service.find_marks(email)
        return BaseResponse(True, '즐겨 찾기 조회 성공', data=mark).to_response()


class PassPointController:
    global pass_point_service

    def __init__(self):
        self.pass_point_service = PassPointService()

    def save_pass_points(self, pass_points, route):
        passpoints = self.pass_point_service.save_pass_point(pass_points, route)
        db.session.bulk_save_objects(passpoints)


class ObjectController:
    global object_service

    def __init__(self):
        self.object_service = ObjectService()

    def save_object(self, objects, route):
        objects = self.object_service.save_object(objects, route)

        db.session.bulk_save_objects(objects)


socketio = SocketIO()


class YoloController:
    def video_detection(self):

        cap = cv2.VideoCapture(0)

        model = YOLO("../YOLO-Weights/best.pt")

        # classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
        #               "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
        #               "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
        #               "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
        #               "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
        #               "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
        #               "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
        #               "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
        #               "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
        #               "teddy bear", "hair drier", "toothbrush"
        #               ]

        classNames = ["green", "red"]

        while True:
            success, img = cap.read()
            results = model(img, stream=True)

            for r in results:
                data = []
                boxes = r.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                    conf = math.ceil((box.conf[0] * 100)) / 100
                    cls = int(box.cls[0])
                    class_name = classNames[cls]
                    label = f'{class_name}{conf}'

                    data.append([x1, y1, x2, y2, label])
                # image
                # ref, buffer = cv2.imencode('.jpg', img)
                # frame = buffer.tobytes()
                # # YOLO 이미지를 전송
                # emit('yolo_frame', frame, broadcast=True)
                # # YOLO 결과 이미지와 변수들을 클라이언트로 전송
                emit('yolo_result', data, broadcast=True)
                # test
                # emit('test','good',broadcast=True)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
