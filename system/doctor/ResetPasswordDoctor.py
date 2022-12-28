from flask import request, abort
from flask_restful import Resource
from system.Models.ActiveDoctor import ActiveDoctor
from system.Models.Doctor import Doctor
from system.utils.otp_required import otp_required
from system.utils.JWT import token_required
from system.Config import Config
from system import db

class ResetPasswordDoctor(Resource):
    @otp_required
    def put(self):
        # checking phone number present or valid or not will be done otp required iteself
        provided_phone = request.args.get("phone")
        email = request.json.get("email")
        new_password = request.json.get("password")

        if not email:
            return {Config.RESPONSE_KEY:"Email not provided"},403

        if not new_password:
            abort(403)

        doctor = Doctor.query.join(ActiveDoctor).filter(
            Doctor.email == email)
        doctor_exist = doctor.first_or_404()
        actual_phone = doctor_exist.phone_no

        if int(actual_phone) != int(provided_phone):
            abort(403)

        doctor_exist.password = new_password
        db.session.commit()

        return {Config.RESPONSE_KEY:"Password Updated"}