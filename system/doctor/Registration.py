from flask import jsonify , make_response
from flask_restful import Resource
from system.doctor.utils.VerifyRegister import verify_register
from system.utils.otp_required import otp_required
from system import db
from system.Models.Doctor import Doctor
from sqlalchemy.exc import IntegrityError
from system.utils.JWT import generate_jwt

class Registration(Resource):
    @verify_register
    @otp_required
    def post(self,*args,**data):
        doctor = Doctor()
        doctor.name = data.get("name")
        doctor.phone_no = data.get("phone number")
        doctor.email = data.get("email")
        doctor.password = data.get("password")
        doctor.reg_no = data.get("registration number")
        doctor.address = data.get("address")
        doctor.category = data.get("category")
        doctor.reff_code = data.get("referal code")
        doctor.profile_pic = data.get("profile picture")
        try:
            db.session.add(doctor)
            db.session.commit()
            token = generate_jwt({"email":doctor.email})
            return jsonify({"token":token})
        except IntegrityError as err:
            return make_response({"status":"Please check your email or registration number"},400)