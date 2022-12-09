from flask_restful import Api
from flask import Blueprint
from system.Vacation.VacationHandler import VacationHandler

vacation = Blueprint("vacation",__name__)
api = Api(vacation)
api.add_resource(VacationHandler,"/") 