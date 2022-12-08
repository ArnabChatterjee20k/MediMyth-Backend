from flask_restful import Resource
from system.Models.Category import Category
from system.Config import Config
from system.category.Schema.GetCategory import GetCategory
class CategoryCreator(Resource):
    def get(self):
        categories = Category.query.al()
        category_schema = GetCategory().dump(categories)
        return category_schema
