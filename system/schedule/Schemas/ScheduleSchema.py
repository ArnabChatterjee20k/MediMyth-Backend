from marshmallow import Schema , fields , validate , EXCLUDE , pre_load , post_load , ValidationError
from system.Config import Config

class ScheduleSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    
    phone_no = fields.Str(validate=validate.Length(equal=10))
    day = fields.Int(required=True,validate=(validate.Range(0,6)))
    specific_week = fields.Int(validate=(validate.Range(1,4)))
    slot_start = fields.Time(required=True)
    slot_end = fields.Time()
    booking_start = fields.Int()
    booking_end  = fields.Int()
    fees = fields.Int()
    patient_limit = fields.Int()
    clinic_name = fields.Str()
    medical_shop = fields.Str()
    address = fields.Str(required=True)

    @pre_load()
    def check(self, data, **kwargs):
        if(self.partial):
        # if self.partial is true we will check whether the data is empty
        ### this is beneficial when we want to update our data
            if(len(data)):
                return data
            raise ValidationError("Data is empty",Config.RESPONSE_KEY)

        ## if self.partial is Fasle we will check either of them should be present
        if not data.get("clinic_name") and not data.get("medical_shop") :
            raise ValidationError('Atleast one of medical shop and clinic name should be present',Config.RESPONSE_KEY)
        
        return data

    @post_load
    def serialize_data(self,data,**kwargs):
        return self.dump(data)