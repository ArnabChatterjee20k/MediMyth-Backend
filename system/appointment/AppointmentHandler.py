from flask_restful import Resource
from system import db
from flask import make_response , request
from system.Models.Appointment import Appointment
from system.Models.Schedule import Schedule
from system.appointment.utils.verifyAppointmentData import verify_appointment
from system.appointment.Schemas.AppointmentDataSchema import AppointmentDataSchema
from system.utils.otp_required import otp_required
from system.Config import Config
import traceback
class AppointmentHandler(Resource):
    def get(self,schedule_id):
        # if date is provided as a filter then we will use it to filter all the appointments in that date
        appointment_date = request.args.get("date")
        filter = {"schedule_id":schedule_id}
        if appointment_date:
            filter["appointment_date"] = appointment_date
        schema = AppointmentDataSchema()
        data = Appointment.query.filter_by(**filter).all()
        ## if schedule not exist then empty array
        return schema.dump(data,many=True)

    @verify_appointment
    @otp_required
    def post(self,schedule_id,**data):
        data = data.get("update")
        exist = Appointment.query.filter_by(schedule_id=schedule_id,**data).first()
        if exist:
            return make_response({Config.RESPONSE_KEY:"already registered"},403)    
        appointment_date = data.get("appointment_date")
        if Appointment.check_booking(schedule_id,appointment_date):
                appointment = Appointment(schedule_id=schedule_id,**data)
                db.session.add(appointment)
                db.session.flush()
                appointment.appointment_id = f"MMA-{appointment.id}"
                db.session.commit()
                return make_response({Config.RESPONSE_KEY:"success","appointment_id":appointment.appointment_id})    
        return make_response({Config.RESPONSE_KEY:"plz check the schedule"},404)