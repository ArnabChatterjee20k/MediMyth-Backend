from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from system.Models.Vacation import Vacation
from system.Models.Schedule import Schedule
from system.Models.ActiveDoctor import ActiveDoctor
from system.Models.Appointment import Appointment
from marshmallow_sqlalchemy.fields import Nested
from system.schedule.Schemas.ScheduleViewSchema import ScheduleDoctorSchema

class VacationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Vacation
        include_relationships = True
        load_instance = True
    
    schedules = Nested(ScheduleDoctorSchema,only=("address",),many=True)