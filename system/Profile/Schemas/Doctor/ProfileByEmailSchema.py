from system.Models.Doctor import Doctor
from system.Models.ActiveDoctor import ActiveDoctor
from system.Models.Schedule import Schedule
from system.Models.Appointment import Appointment
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
class ProfileByEmailSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Doctor
        exclude=("_password",)