from flask_restful import Resource
from flask import make_response , jsonify , request
from system import db
from system.Models.Doctor import Doctor
from system.Models.Schedule import Schedule
from system.schedule.Schemas.ScheduleDoctorSchema import ScheduleDoctorSchema
from system.schedule.utils.VerifyScheduleUpdate import verify_update_schedule
from system.utils.JWT import token_required
from system.Config import Config

class ScheduleAccess(Resource):
    """This is for doctor"""
    @verify_update_schedule
    @token_required
    def put(self,schedule_id,*args,**data):
        required_data = data.get("update")
        email = data.get("email")
        schedule = Schedule(**required_data) # constructing Schedule object 
        if schedule.check_slot(doctor_id=Schedule().active_doctor_by_email(email)) or schedule.data_exists():
            return make_response({Config.RESPONSE_KEY:"schedule already exists in this time"},403)
        try:
            Schedule().check_and_update(schedule_id,email,**required_data)
            print("put",args,data)
        except:
            return make_response({Config.RESPONSE_KEY:"Not found"},404)

        ##Todo: send otp to all patient appointed this meeting
        return make_response({Config.RESPONSE_KEY:"updated"},200)
    
    @token_required
    def delete(self,schedule_id,**data):
        email = data.get("email")
        Schedule().check_and_delete(email,schedule_id)
        return make_response({Config.RESPONSE_KEY:"deleted"},200)