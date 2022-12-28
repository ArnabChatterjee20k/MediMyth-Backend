from flask_restful import Api
from flask import Blueprint
from system.reset_password.ResetPassword import ResetPassword

reset_password = Blueprint("reset_password",__name__)
api = Api(reset_password)

api.add_resource(ResetPassword,"/reset")