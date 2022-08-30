from flask import jsonify , request
from flask_restful import Resource
from system.doctor.utils.VerifyRegister import verify
from system.utils.otp_required import otp_required


class Register(Resource):
    @verify
    @otp_required
    def post(self,*args,**data):
        return jsonify(data)