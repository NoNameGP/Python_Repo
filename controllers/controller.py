from flask_restful import Resource, reqparse
from flask import request
from models.model import db
from flask_login import logout_user, login_required
from services.service import *
from dto.dto import *


class UserResource(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
        parser.add_argument('password', type=str, required=True, help='Password cannot be blank')
        args = parser.parse_args()

        user_service = UserService()
        user, response = UserService.register_user(user_service, args)

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
        UserService.login_user(user_service, json_data)

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

        passpoint_service = PassPointService()
        passpoints = passpoint_service.save_pass_point(routeReq.pass_points, route)

        object_service = ObjectService()
        objects = object_service.save_object(routeReq.objects, route)

        db.session.bulk_save_objects(passpoints)
        db.session.bulk_save_objects(objects)

        db.session.commit()

        return {'success': True, 'message': '경로 추가 완료'}, 200
