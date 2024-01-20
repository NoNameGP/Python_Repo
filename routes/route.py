from flask_restful import Api
from controllers.controller import *


class Route:
    def __init__(self,app):
        api = Api(app)
        api.add_resource(UserResource, '/user')
        api.add_resource(Session, '/session')
        api.add_resource(RouteResource, "/route", '/route/<string:departure>/<string:arrival>')
        api.add_resource(MarkResourece, '/mark', '/mark/<string:email>')