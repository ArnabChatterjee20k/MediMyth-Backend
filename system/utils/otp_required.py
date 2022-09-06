from system.utils.verifyOTP import check
from functools import wraps
from flask import request , make_response , jsonify
from system.Config import Config

def otp_required(function):
    @wraps(function)
    def inner(*args,**kwargs):
        token = request.headers.get("token")
        phone_number = request.args.get("phone")
        if not token:
            message = jsonify({Config.RESPONSE_KEY:"OTP not provided"})
            return make_response(message,400)
        if not phone_number:
            message = jsonify({Config.RESPONSE_KEY:"phone number not provided"})
            return make_response(message,400)
        try:
            if Config.PRODUCTION:
                check(code=token,phone=phone_number)
            return function(*args,**kwargs)
        except Exception as e:
            print(e)
            message = jsonify({Config.RESPONSE_KEY:"invlaid otp"})
            return make_response(message,400)
    return inner