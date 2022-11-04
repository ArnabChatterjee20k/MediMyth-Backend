from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from system.Models.ActiveDoctor import ActiveDoctor

class ActiveDoctorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ActiveDoctor