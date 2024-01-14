from models.model import User, Route, PassPoint, Object, Mark
from flask_login import login_user


class UserService:

    def register_user(self, args):
        user = User.find_user(args['email'])

        if user:
            return None, {'success': False, 'message': '이미 가입된 이메일입니다.'}

        new_user = User(email=args['email'], password=args['password'])
        new_user.set_password(args['password'])

        return new_user, {'success': True, 'message': '가입 가능한 이메일입니다.'}

    def login_user(self, json_data):
        user = User.find_user(json_data['email'])

        if user and user.check_password(json_data['password']):
            login_user(user)
            return {'success': True, 'message': '로그인 성공'}, 200


class RouteService:
    def save_route(self, routeDTO):
        user = User.find_user(routeDTO.email)

        return Route(user, routeDTO.start_point, routeDTO.end_point)


class PassPointService:
    def save_pass_point(self, pass_points, route):
        return [PassPoint(route, **passpoint) for passpoint in pass_points]


class ObjectService:
    def save_object(self, objects, route):
        return [Object(route, **object) for object in objects]


class MarkService:
    def save_object(self, mark_dto):
        user = User.find_user(mark_dto.email)

        return Mark(user, mark_dto.mark_name, mark_dto.end_point)
