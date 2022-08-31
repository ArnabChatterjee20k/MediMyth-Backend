from flask_restful import Api
from flask import Blueprint
from system.doctor.Registration import Registration
doctor = Blueprint("doctor",__name__)
api = Api(doctor)
api.add_resource(Registration,"/register")