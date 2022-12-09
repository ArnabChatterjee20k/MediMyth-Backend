from flask_restful import Resource
from system.Models.Vacation import Vacation

class VacationHandler(Resource):
    def get(self):
        return "hellow"