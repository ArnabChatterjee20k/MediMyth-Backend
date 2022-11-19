import email
from flask_restful import Resource
from flask import make_response
from system.doctor.utils.VerifyLogin import verify_login
from system.doctor.utils.VerifyUpdate import verify_update
from system.Models.Doctor import Doctor
from system.utils.JWT import generate_jwt , token_required
from system import db
from system.Config import Config
class Account(Resource):
    @verify_login
    def get(self,**data):
        data = data.get("update")
        email = data.get("email")
        password = data.get("password")
        try:
            doctor = Doctor().check_password(email=email,password=password)
            if doctor:
                return make_response({"token":generate_jwt({"email":email})})
            return make_response({Config.RESPONSE_KEY:"Invalid Password"},400)
        except:
            return make_response({Config.RESPONSE_KEY:"Email not found"},404)
    
    @verify_update
    @token_required
    def put(self,**data):
        # since the incoming data is not fully required so we are implementing 
        # updated data is in update key of data
        update_data = data.get("update")
        email = data.get("email")

        # Doctor().update_data(data.get("email"),update_data)
        doctor = Doctor.query.filter_by(email=email)
        doctor.first_or_404() ## for checking the existance

        doctor.update(update_data)

        db.session.commit()
        response = {Config.RESPONSE_KEY:"updated"}
        new_email = update_data.get("email")
        if new_email:
            response["token"] = generate_jwt({"email":new_email})            
        return make_response(response,200) #to generate the response with the new email if email updated else status
    
    @token_required
    def delete(self,**data):
        email = data.get("email")
        doctor = Doctor.query.filter_by(email=email).first_or_404() # if doctor not found then 404
        db.session.delete(doctor)
        db.session.commit()

        return make_response({Config.RESPONSE_KEY:"deleted"},200)
