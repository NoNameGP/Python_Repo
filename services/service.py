from models.model import User, Route, PassPoint, Object, Mark
from flask_login import login_user


class UserService:

    def register_user(self, userDTO):
        user = User.find_user(userDTO.email)

        if user:
            return None, {'success': False, 'message': '이미 가입된 이메일입니다.'}

        new_user = User(userDTO.email, userDTO.password)
        new_user.set_password(userDTO.password)

        return new_user, {'success': True, 'message': '가입 가능한 이메일입니다.'}

    def login_user(self, userDTO):
        user = User.find_user(userDTO.email)

        if user and user.check_password(userDTO.password):
            login_user(user)
            return {'success': True, 'message': '로그인 성공'}, 200


class RouteService:
    def save_route(self, routeDTO):
        user = User.find_user(routeDTO.email)

        return Route(user, routeDTO.departure, routeDTO.arrival)

    def find_route(self, departure, arrival):
        global best_route
        min = 1000
        for route in Route.find_route(departure, arrival):
            if min > len(route.find_objects()):
                best_route = route
                min = len(route.find_objects())

        return best_route


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

    def find_marks(self, email):
        user = User.find_user(email)
        return [mark.to_dict()for mark in user.find_user_marks()]
