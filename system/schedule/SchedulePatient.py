from flask_restful import Resource
from system.Models.Schedule import Schedule
from system.schedule.Schemas.ScheduleViewSchema import SchedulePatientSchema

class SchedulePatient(Resource):
    def get(self,active_doctor_id):
        schedules = Schedule.query.filter(Schedule.active_doctor_id==active_doctor_id).all()
        schema = SchedulePatientSchema(many=True)
        return schema.dump(schedules)
