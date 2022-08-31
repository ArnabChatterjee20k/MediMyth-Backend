from marshmallow import Schema , fields, validate , post_load , EXCLUDE
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
    
    @post_load
    def serialize_data(self,data,**kwargs):
        return self.dump(data)