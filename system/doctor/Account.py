from flask_restful import Resource
from flask import make_response
from system.doctor.utils.VerifyLogin import verify
from system.Models.Doctor import Doctor
from system.utils.JWT import generate_jwt
class Account(Resource):
    @verify
    def get(self,**data):
        email = data.get("email")
        password = data.get("password")
        try:
            doctor = Doctor().check_password(email=email,password=password)
            if doctor:
                return make_response({"token":generate_jwt({"email":email})})
            return make_response({"status":"Invalid Password"},400)
        except:
            return make_response({"status":"Email not found"},404)