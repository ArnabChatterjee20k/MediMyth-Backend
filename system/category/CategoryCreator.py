from flask import jsonify , make_response
from flask_restful import Resource
from system.Models.Category import Category
from system.category.Schema.GetCategory import GetCategory
class CategoryCreator(Resource):
    def get(self):
        categories = Category.query.all()
        print(categories)
        category_schema = GetCategory().dump(categories,many=True)
        return make_response(jsonify(category_schema),200)
