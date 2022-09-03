from flask_restful import Resource
from flask import make_response
from system import db
from system.Models.Schedule import Schedule
from system.Models.Doctor import Doctor
from system.schedule.utils.VerifySchedule import verify_schedule
from system.utils.JWT import token_required


class Scheduler(Resource):
    @verify_schedule
    @token_required
    def post(self,**data):
        print(data)
        email = data.get("email")
        try:
            doctor = Doctor.query.filter_by(email=email,active=True).first_or_404() # seeing if doctor is active or not
        except:
            return make_response({"status":"doctor not found"},404)
        doctor_id = doctor.id

        required_data = data.get("update")
        required_data["doctor_id"] = doctor_id
        schedule = Schedule(**required_data)

        try:
            db.session.add(schedule)
            db.session.commit()            
        except:
            return make_response({"status":"internal server error"},500)
        
        
