from flask_restful import Resource, reqparse
from flask import request
from models.model import db
from flask_login import logout_user, login_required, login_user
from services.service import *
from dto.dto import *
from controllers.BaseResponse import BaseResponse


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
