from marshmallow import Schema , fields , validate , EXCLUDE , pre_load , post_load , ValidationError

class ScheduleSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    
    phone_no = fields.Str(validate=validate.Length(equal=10))
    day = fields.Int(required=True,validate=(validate.Range(0,6)))
    specific_week = fields.Int(validate=(validate.Range(1,4)))
    slot_start = fields.Time(required=True)
    slot_end = fields.Int()
    booking_start = fields.Int()
    booking_end  = fields.Int()
    fees = fields.Int()
    limit = fields.Int()
    clinic_name = fields.Str()
    medical_shop = fields.Str()
    address = fields.Str(required=True)

    @pre_load()
    def check(self, data, **kwargs):
        ## either of them should be present
        if not data.get("clinic_name") and not data.get("medical_shop") :
            raise ValidationError('Atleast one of medical shop and clinic name should be present',"_missing")
        return data

    @post_load
    def serialize_data(self,data,**kwargs):
        return self.dump(data)