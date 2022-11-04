from system.Models.Doctor import Doctor
from system.Models.ActiveDoctor import ActiveDoctor
from system.Models.Schedule import Schedule
from system.Models.Appointment import Appointment
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from system.Profile.Schemas.Doctor.ActiveDoctorSchema import ActiveDoctorSchema
from marshmallow_sqlalchemy.fields import Nested
class ProfileByEmailSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Doctor
        ordered = True
        exclude=("_password",)
    active_id = Nested(ActiveDoctorSchema,many=True,only=("active_doctor_id",))