from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models.model import db
from controllers.controller import TodoListResource


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    return app


app = create_app()
api = Api(app)
api.add_resource(TodoListResource, '/todos')
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
