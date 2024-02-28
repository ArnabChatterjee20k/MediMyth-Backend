from flask_restful import Resource , abort
from system.Config import Config

from system.utils.generateOTP import send_sms
class OTP(Resource):
    """For sending otp verification can be done by importing verifyOTP"""
    def get(self,phone):
        try:
            if(Config.PRODUCTION and Config.OTP):
                send_sms.delay(phone)
            return {Config.RESPONSE_KEY : "success"}
        except Exception as e:
            print(e)
            return abort(400)