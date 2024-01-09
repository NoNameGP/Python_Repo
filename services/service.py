from models.model import User
from flask_login import login_user


class UserService:

    def register_user(self, args):
        user = User.query.filter_by(email=args['email']).first()

        if user:
            return None, {'success': False, 'message': '이미 가입된 이메일입니다.'}

        new_user = User(email=args['email'], password=args['password'])
        new_user.set_password(args['password'])

        return new_user, {'success': True, 'message': '가입 가능한 이메일입니다.'}

    def login_user(self, json_data):
        user = User.query.filter_by(email=json_data['email']).first()

        if user and user.check_password(json_data['password']):
            login_user(user)
            return {'success': True, 'message': '로그인 성공'}, 200
