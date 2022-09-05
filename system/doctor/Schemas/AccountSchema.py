from marshmallow import Schema , fields, validate , post_load , EXCLUDE , pre_load , ValidationError
class AccountSchema(Schema):
    class Meta:
        unknown = EXCLUDE # excluding the unknown field
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone_number = fields.Str(required=True,validate=validate.Length(equal=10),data_key="phone number")
    referal_code = fields.Str(data_key="referal code")
    reg_no = fields.Str(required=True,data_key="registration number")
    address = fields.Str(required=True)
    category = fields.Str(required=True)
    password = fields.Str(required=True)
    profile_picture = fields.Raw(type="file",data_key="profile picture")
    
    @pre_load
    def check(self,data,**kwargs):
        if(self.partial):
        # if self.partial is true we will check whether the data is empty
        ### this is beneficial when we want to update our data
            if(len(data)):
                return data
            raise ValidationError("Data is empty","status")
        return data
    @post_load
    def serialize_data(self,data,**kwargs):
        return self.dump(data)