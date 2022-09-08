from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from system.Models.Appointment import Appointment

class AppointmentDataSchema(SQLAlchemyAutoSchema):
        class Meta:
            model = Appointment
            include_relationships = True
            load_instance = True