from flask_restful import Resource, reqparse
from flask import request
from models.model import db
from flask_login import logout_user, login_required
from services.service import *
from dto.dto import *


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

        return {'success': True, 'message': '회원가입과 로그인 성공'}, 200


class Session(Resource):
    def post(self):
        json_data = request.get_json()

        user_service = UserService()
        UserService.login_user(user_service, UserDTO(**json_data))

        return {'success': True, 'message': 'Login successful'}, 200

    @login_required
    def patch(self):
        logout_user()
        return {'success': True, 'message': 'Logout successful'}, 200


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

        return {'success': True, 'message': '경로 추가 완료'}, 200


class MarkResourece(Resource):
    def post(self):
        data = request.get_json()

        mark_data = MarkDTO(**data)

        mark_service = MarkService()

        mark = mark_service.save_object(mark_data)

        db.session.add(mark)
        db.session.commit()

        return {'success': True, 'message': '즐겨찾기 추가 완료'}, 200


class PassPointController:
    global pass_point_service

    def __init__(self):
        self.pass_point_service = PassPointService()

    def save_pass_points(self, pass_points, route):
        passpoints = pass_point_service.save_pass_point(pass_points, route)
        db.session.bulk_save_objects(passpoints)


class ObjectController:
    global object_service

    def __init__(self):
        self.object_service = ObjectService()

    def save_object(self, objects, route):
        objects = object_service.save_object(objects, route)

        db.session.bulk_save_objects(objects)
