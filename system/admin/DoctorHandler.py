from flask_restful import Resource
from system.Models.Doctor import Doctor
from flask import make_response
from sqlalchemy.exc import IntegrityError
from system.Config import Config

class DoctorHandler(Resource):
    def put(self,id):
        try:
            return make_response({Config.RESPONSE_KEY:Doctor.set_active(id)})
        except IntegrityError:
            return make_response({Config.RESPONSE_KEY:"Doctor is already active"},403)
            