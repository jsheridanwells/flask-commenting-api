from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Category import Category

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Hello, '/Hello')
api.add_resource(Category, '/Category')
