from marshmallow import Schema , fields , post_load , EXCLUDE , pre_load , ValidationError
from system.appointment.utils.Date import Date
from system.Config import Config
from system.utils.convert_str_to_date import convert_str_to_date

class VacationCreationSchema(Schema):
    class Meta:
        unknown = EXCLUDE # excluding the unknown field
    start = Date(required=True,format=Config.UTC_String_Format)
    end = Date(required=True,format=Config.UTC_String_Format)
    reason = fields.Str(allow_none=True)
    # a list of vacation ids should be sent
    schedules_ids = fields.List(fields.Int(),required=True)

    @pre_load
    def check(self,data,**kwargs):
        start = convert_str_to_date(data.get("start"))
        end = convert_str_to_date(data.get("end"))
        
        check = start>=end

        if(check):
            raise ValidationError("Start Date must be before End date")
        
        return data