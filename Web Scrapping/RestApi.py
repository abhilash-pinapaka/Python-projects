from flask import Flask
from flask_restful import Api, Resource, Namespace


app = Flask(__name__)

api = Api(
    title='Rest API', version='1.0',
    description='A simple  application exposing the Potato Market to the web'
)


class Checks(Resource):

    def get(self):
        pass
