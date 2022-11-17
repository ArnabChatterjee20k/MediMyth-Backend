from flask_restful import Api
from flask import Blueprint

from system.admin.DoctorHandler import DoctorHandler

doctor_handler = Blueprint("doctorhandler", __name__)
api = Api(doctor_handler)
api.add_resource(DoctorHandler,"/doctors/<int:id>")