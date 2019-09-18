import tornado.web
import config

from tornado.escape import json_decode
from services import LoanService

# Constants of the module
_bad_request_code = 400
_bad_request_message = 'Bad Request. Your browser sent a request that this server could not understand.'


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(config.version)


class LoanHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        methods = 'POST, OPTIONS'
        headers = 'access-control-allow-origin,authorization,content-type,x-requested-with'
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', methods)
        self.set_header('Access-Control-Allow-Headers', headers)

    def options(self):
        self.set_status(204)
        self.finish()

    def post(self):
        try:
            request = json_decode(self.request.body)
            self.validate_request(request)
            result = LoanService().validate_loan(request['amount'])
            self.write(result)
        except:
            self.clear()
            self.set_status(_bad_request_code)
            self.write(_bad_request_message)

    def validate_request(self, request):
        if not request['amount']:
            raise ValueError(_bad_request_message)
        else:
            request['amount'] = int(float(request['amount']))
