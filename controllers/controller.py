from flask_restful import Resource
from flask import request
from models.model import User,db


class TodoListResource(Resource):
    def get(self):
        todos = User.query.all()
        todo_dict = {}
        for todo in todos:
            todo_dict[todo.id] = todo.email
        return todo_dict

    def post(self):
        json_data = request.get_json()
        if not json_data or 'email' not in json_data:
            return {'error': 'User is required'}, 400

        new_user = User(json_data['email'],json_data['password'])
        db.session.add(new_user)
        db.session.commit()

        return {'id': new_user.id, 'task': new_user.email, 'password': new_user.password}
