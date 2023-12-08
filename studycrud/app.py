from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite 데이터베이스
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

todos = {}


class TodoResource(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['task']
        return {todo_id: todos[todo_id]}

    def delete(self, todo_id):
        del todos[todo_id]
        return {'result': True}


class TodoListResource(Resource):
    def get(self):
        return todos

    def post(self):
        json_data = request.get_json()
        if not json_data or 'task' not in json_data:
            return {'error': 'Task is required'}, 400

        todo_id = max(map(int, todos.keys())) + 1 if todos else 1
        todos[todo_id] = json_data['task']
        return {todo_id: todos[todo_id]}


api.add_resource(TodoListResource, '/todos')
api.add_resource(TodoResource, '/todos/<int:todo_id>')
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Todo {self.id}: {self.task}"


if __name__ == '__main__':
    app.run(debug=True)
