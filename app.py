from flask import request
from flask_restful import Resource
from database import db,api,app
from model import User


class TodoListResource(Resource):
    def get(self):
        todos = User.query.all()
        todo_dict = {}
        for todo in todos:
            todo_dict[todo.id] = todo.task
        return todo_dict

    def post(self):
        json_data = request.get_json()
        if not json_data or 'user' not in json_data:
            return {'error': 'User is required'}, 400

        new_user = User(email=json_data['email'])
        db.session.add(new_user)
        db.session.commit()

        return {'id': new_user.id, 'task': new_user.task}



api.add_resource(TodoListResource, '/todos')




if __name__ == '__main__':
    app.run(debug=True)