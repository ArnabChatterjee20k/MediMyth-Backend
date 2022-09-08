from flask_restful import Resource
from system import db
from flask import make_response
from system.Models.Appointment import Appointment
from system.appointment.utils.verifyAppointmentData import verify_appointment
from system.utils.otp_required import otp_required
from system.Config import Config
import traceback
class AppointmentHandler(Resource):
    @verify_appointment
    @otp_required
    def post(self,schedule_id,**data):
        data = data.get("update")
        exist = Appointment.query.filter_by(**data).first()
        if exist:
            return make_response({Config.RESPONSE_KEY:"already registered"},403)    
        if Appointment.check_booking(schedule_id):
            try:
                appointment = Appointment(schedule_id=schedule_id,**data)
                db.session.add(appointment)
                db.session.flush()
                appointment.appointment_id = f"MMA-{appointment.id}"
                db.session.commit()
                return make_response({Config.RESPONSE_KEY:"success","appointment_id":appointment.appointment_id})    
            except Exception as e:
                print(e)
                traceback.print_exc()
                return make_response({Config.RESPONSE_KEY:"internal server error"},500)    
        return make_response({Config.RESPONSE_KEY:"plz check the schedule"},404)