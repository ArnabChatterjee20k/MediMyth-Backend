from flask import jsonify , make_response
from flask_restful import Resource
from system.doctor.utils.VerifyRegister import verify_register
from system.utils.otp_required import otp_required
from system import db
from system.Models.Doctor import Doctor
from sqlalchemy.exc import IntegrityError
from system.utils.JWT import generate_jwt
from system.Config import Config
class Registration(Resource):
    @verify_register
    def post(self,*args,**data):
        data = data.get("update")
        # data consists of many fields which we cant pass in the doctor schema
        # but data will surely contain columns which are present even in Doctor table

        doctor = Doctor(**data)
        # doctor.name = data.get("name")
        # doctor.phone_no = data.get("phone_no")
        doctor.email = data.get("email")
        # doctor.password = data.get("password")
        # doctor.reg_no = data.get("reg_no")
        # doctor.address = data.get("address")
        # doctor.category = data.get("category")
        # doctor.reff_code = data.get("referal code")
        # doctor.profile_pic = data.get("profile picture")
        
        try:
            db.session.add(doctor)
            db.session.commit()
            token = generate_jwt({"email":doctor.email})
            return jsonify({"token":token})
        except IntegrityError as err:
            print(err)
            return make_response({Config.RESPONSE_KEY:"Please check your email or registration number"},400)