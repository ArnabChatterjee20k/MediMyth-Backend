from flask_restful import Resource , abort
from flask import jsonify

from system.utils.generateOTP import send_sms
class OTP(Resource):
    """For sending otp verification can be done by importing verifyOTP"""
    def get(self,phone):
        try:
            send_sms(phone)
        except:
            return abort(400)