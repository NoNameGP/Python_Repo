from flask_restful import Resource
from flask import request
from models.model import User, db
from flask_login import login_user, logout_user, current_user, login_required
from flask_restful import reqparse


class TodoListResource(Resource):
    def get(self):
        todos = User.query.all()
        todo_dict = {}
        for todo in todos:
            todo_dict[todo.id] = todo.email
        return repr(todos)

    def post(self):
        json_data = request.get_json()
        if not json_data or 'email' not in json_data:
            return {'error': 'User is required'}, 400

        new_user = User(json_data['email'], json_data['password'])
        db.session.add(new_user)
        db.session.commit()

        return {'id': new_user.id, 'task': new_user.email, 'password': new_user.password}


class UserResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
        parser.add_argument('password', type=str, required=True, help='Password cannot be blank')
        args = parser.parse_args()

        user = User.query.filter_by(email=args['email']).first()

        if user:
            return {'success': False, 'message': '이미 가입된 이메일입니다.'}, 400

        new_user = User(email=args['email'], password=args['password'])
        new_user.set_password(args['password'])
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return {'success': True, 'message': '회원가입과 로그인 성공'}, 200


class Session(Resource):
    def post(self):
        json_data = request.get_json()

        user = User.query.filter_by(email=json_data['email']).first()

        if user and user.check_password(json_data['password']):
            login_user(user)
            return {'success': True, 'message': '로그인 성공'}, 200

        return {'success': False, 'message': 'Login failed'}, 401

    @login_required
    def patch(self):
        logout_user()
        return {'success': True, 'message': 'Logout successful'}, 200
