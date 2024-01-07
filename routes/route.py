from flask_restful import Api
from controllers.controller import *


class Route:
    def __init__(self,app):
        api = Api(app)
        api.add_resource(TodoListResource, '/todos')
        api.add_resource(UserResource, '/user')
        api.add_resource(Session, '/session')
