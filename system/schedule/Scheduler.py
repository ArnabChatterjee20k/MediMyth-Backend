from flask_restful import Resource
from flask import make_response , jsonify , request
from system import db
from system.Models.Doctor import Doctor
from system.Models.Schedule import Schedule
from system.schedule.utils.VerifySchedule import verify_schedule
from system.schedule.Schemas.ScheduleDoctorSchema import ScheduleDoctorSchema
from system.schedule.utils.VerifyScheduleUpdate import verify_update_schedule
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

        # if schedule already exists
        ## TODO: need to be talked about the clinic_name and medical_shop
        if(schedule.data_exists()):
            return make_response({"status":"schedule already exists"},403)

        try:
            db.session.add(schedule)
            db.session.commit()       
            return make_response({"status":"success"},200)   
        except:
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
    
    @verify_update_schedule
    @token_required
    def put(self,**data):
        required_data = data.get("update")
        email = data.get("email")
        schedule_id = request.args.get("schedule")
        try:
            Schedule().check_and_update(schedule_id,email,**required_data)
        except:
            return make_response({"status":"Not found"},404)

        ##Todo: send otp to all patient appointed this meeting
        return make_response({"status":"updated"},200)