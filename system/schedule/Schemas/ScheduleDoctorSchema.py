from system.Models.Schedule import Schedule
## Appointment model needed to be imported here as Schedule Schema is linked to Appointment
from system.Models.Appointment import Appointment
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class ScheduleDoctorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Schedule
        include_relationships = True
        load_instance = True