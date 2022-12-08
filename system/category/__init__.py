from flask_restful import Api
from flask import Blueprint
from system.category.CategoryCreator import CategoryCreator

category = Blueprint("category",__name__)
api = Api(category)
api.add_resource(CategoryCreator,"/")