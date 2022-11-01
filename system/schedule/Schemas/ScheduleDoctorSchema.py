from system.Models.Schedule import Schedule
## Appointment model needed to be imported here as Schedule Schema is linked to Appointment
from system.Models.Appointment import Appointment
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested


class Appointmentschema(SQLAlchemyAutoSchema):
    class Meta:
        model = Appointment
        ordered = True


class ScheduleDoctorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Schedule
        ordered = True
    # must be same name as the relationship attribute between Schedule and Appointment Table
    appointment_data = Nested(Appointmentschema,  many=True , only=("id","appointment_date"))