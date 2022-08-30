from flask import jsonify
from flask_restful import Resource
from system.doctor.utils.VerifyRegister import verify
class Register(Resource):
    @verify
    def post(self,*args,**data):
        return jsonify(data)
        