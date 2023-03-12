from datetime import datetime
from flask_restful import Resource
from flask import make_response, jsonify, request
from system import db
from system.Models.Doctor import Doctor
from system.Models.Schedule import Schedule
from system.schedule.utils.VerifySchedule import verify_schedule
from system.schedule.Schemas.ScheduleViewSchema import ScheduleDoctorSchema
from system.utils.JWT import token_required
from system.Config import Config
import sys
from system.Models.ActiveDoctor import ActiveDoctor


class Scheduler(Resource):
    """This is for doctor"""
    @verify_schedule
    @token_required
    def post(self, **data):
        print(data)
        email = data.get("email")

        try:
            doctor = Doctor.query.filter_by(
                email=email).first_or_404()
            # seeing if doctor is active or not. if not active we will not search in active_doctor table
        except:
            return make_response({Config.RESPONSE_KEY: "doctor not found"}, 404)
        doctor_id = doctor.active_id.first().id

        required_data = data.get("update")
        required_data["active_doctor_id"] = doctor_id

        # checking if phone number present in the schedule or not
        if not required_data.get("phone_no"):
            required_data["phone_no"] = doctor.phone_no

        try:
            error_exist, errors = Schedule.create_schedule(required_data)
            if (error_exist):
                return {Config.RESPONSE_KEY: errors}, 403
            return make_response({Config.RESPONSE_KEY: "success"}, 200)
        except Exception as e:
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_tb.tb_lineno)

            return make_response({Config.RESPONSE_KEY: "internal server error"}, 500)

    @token_required
    def get(self, **data):
        email = data.get("email")
        print(data)
        try:
            doctor = Doctor.query.join(ActiveDoctor).filter(
                Doctor.email == email).first_or_404()
            # seeing if doctor is active or not. if not active we will not search in active_doctor table
        except Exception as e:
            print(e)
            return make_response({Config.RESPONSE_KEY: "doctor not found"}, 404)
        doctor_id = doctor.active_id.first().id

        schema = ScheduleDoctorSchema()

        query = request.args
        start = query.get("start")
        end = query.get("end")
        if start and end:
            data = Schedule.get_schedules_between_dates(
                active_doctor_id=doctor_id, start=start, end=end)
            return jsonify((schema.dump(data, many=True)))

        data = Schedule.query.filter_by(active_doctor_id=doctor_id).all()
        return jsonify((schema.dump(data, many=True)))
