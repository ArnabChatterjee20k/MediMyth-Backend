from flask_restful import Api
from flask import Blueprint
from system.Profile.DoctorProfileById import DoctorProfileById
from system.Profile.DoctorProfileByEmail import DoctorProfileByEmail

profile = Blueprint("doctor_profile_by_id",__name__)
api = Api(profile)

api.add_resource(DoctorProfileById,"/doctors/<int:id>") # for patients
api.add_resource(DoctorProfileByEmail,"/doctors/view") # for doctors themseleves