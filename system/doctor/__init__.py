from flask_restful import Api
from flask import Blueprint
from system.doctor.Registration import Registration
from system.doctor.Account import Account
from system.doctor.ResetPasswordDoctor import ResetPasswordDoctor
from system.doctor.UploadPicture import UploadPicture
doctor = Blueprint("doctor",__name__)
api = Api(doctor)
api.add_resource(Registration,"/register") 
api.add_resource(Account,"/") 
api.add_resource(ResetPasswordDoctor,"/password")
api.add_resource(UploadPicture,"/picture")