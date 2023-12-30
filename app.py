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

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Todo {self.id}: {self.task}"


class TodoListResource(Resource):
    def get(self):
        todos = Todo.query.all()
        todo_dict = {}
        for todo in todos:
            todo_dict[todo.id] = todo.task
        return todo_dict

    def post(self):
        json_data = request.get_json()
        if not json_data or 'task' not in json_data:
            return {'error': 'Task is required'}, 400

        new_todo = Todo(task=json_data['task'])
        db.session.add(new_todo)
        db.session.commit()

        return {'id': new_todo.id, 'task': new_todo.task}



api.add_resource(TodoListResource, '/todos')




if __name__ == '__main__':
    app.run(debug=True)