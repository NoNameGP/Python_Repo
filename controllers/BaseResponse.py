from flask import make_response, jsonify


class BaseResponse:
    def __init__(self, success, message, status_code=200, data=None):
        self.success = success
        self.message = message
        self.data = data
        self.status_code = status_code

    def to_dict(self):
        response_dict = {
            'success': self.success,
            'message': self.message,
        }
        if self.data is not None:
            response_dict['data'] = self.data

        return response_dict

    def to_response(self):
        return make_response(jsonify(self.to_dict()), self.status_code)