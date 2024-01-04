from flask_restful import Api
from controllers.controller import TodoListResource


class Route:
    def __init__(self,app):
        api = Api(app)
        api.add_resource(TodoListResource, '/todos')
