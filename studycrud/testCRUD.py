from flask import Flask
from flask_restful import Resource, Api
from secure_check import authenticate,identity
from flask_jwt_extended import JWTManager, jwt_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretary'

api = Api(app)
jwt = JWTManager(app)


class Helloworld(Resource):

    def get(self):
        return {'hello': 'world'}


api.add_resource(Helloworld, '/')

puppies = []


class PuppyNames(Resource):
    def get(self, name):

        for pup in puppies:
            if pup['name'] == name:
                return pup
        return {'name': None},404

    def post(self, name):

        pup = {'name': name}

        puppies.append(pup)

        return pup

    def delete(self, name):

        for ind, pup in enumerate(puppies):
            if pup['name'] == name:
                deleted_pup = puppies.pop(ind)
                return {'note': 'delete success'}


class AllNames(Resource):
    @jwt_required()
    def get(self):
        return {'puppies': puppies}


api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllNames, '/puppies')
api.add_resource(authenticate, "/login")

if __name__ == '__main__':
    app.run(debug=True)
