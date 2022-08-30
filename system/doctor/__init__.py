from flask_restful import Api
from flask import Blueprint
from system.doctor.Register import Register
doctor = Blueprint("doctor",__name__)
api = Api(doctor)
api.add_resource(Register,"/register")