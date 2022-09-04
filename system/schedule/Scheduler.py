from flask_restful import Resource
from flask import make_response , request , jsonify
from system import db
from system.Models.Doctor import Doctor
from system.Models.Schedule import Schedule
from system.schedule.utils.VerifySchedule import verify_schedule
from system.schedule.Schemas.ScheduleDoctorSchema import ScheduleDoctorSchema
from system.utils.JWT import token_required


class Scheduler(Resource):
    """This is for doctor"""
    @verify_schedule
    @token_required
    def post(self,**data):
        email = data.get("email")
        try:
            doctor = Doctor.query.filter_by(email=email,active=True).first_or_404() 
            # seeing if doctor is active or not. if not active we will not search in active_doctor table
        except:
            return make_response({"status":"doctor not found"},404)
        doctor_id = doctor.active_id.first().id

        required_data = data.get("update")
        required_data["active_doctor_id"] = doctor_id
        schedule = Schedule(**required_data)

        try:
            db.session.add(schedule)
            db.session.commit()            
        except Exception:
            return make_response({"status":"internal server error"},500)

    @token_required
    def get(self,**data):
        email = data.get("email")
        try:
            doctor = Doctor.query.filter_by(email=email,active=True).first_or_404() 
            # seeing if doctor is active or not. if not active we will not search in active_doctor table
        except:
            return make_response({"status":"doctor not found"},404)
        doctor_id = doctor.active_id.first().id

        schema = ScheduleDoctorSchema()
        data = Schedule.query.filter_by(active_doctor_id=doctor_id).all()
        return jsonify((schema.dump(data,many=True)))