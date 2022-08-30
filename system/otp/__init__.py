from flask_restful import Api
from flask import Blueprint
from system.otp.OTP import OTP
otp = Blueprint("otp",__name__)
api = Api(otp)
api.add_resource(OTP,"/<phone>")