from marshmallow import Schema , fields, validate , post_load , EXCLUDE , pre_load , ValidationError
from system.Config import Config
class AccountSchema(Schema):
    class Meta:
        unknown = EXCLUDE # excluding the unknown field
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone_no = fields.Str(required=True,validate=validate.Length(equal=10))
    reff_code = fields.Str(allow_none=True)
    reg_no = fields.Str(required=True)
    address = fields.Str(required=True)
    category = fields.Str(required=True)
    description = fields.Str(allow_none=True)
    password = fields.Str(required=True)
    profile_pic = fields.Raw(type="file",allow_none=True)
    
    email_visibility = fields.Bool()
    reg_no_visibility = fields.Bool()
    phone_no_visibility = fields.Bool()
    @pre_load
    def check(self,data,**kwargs):
        if(self.partial):
        # if self.partial is true we will check whether the data is empty
        ### this is beneficial when we want to update our data
            if(len(data)):
                return data
            raise ValidationError("Data is empty",Config.RESPONSE_KEY)
        return data
    @post_load
    def serialize_data(self,data,**kwargs):
        return self.dump(data)