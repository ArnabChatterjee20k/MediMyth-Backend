from marshmallow import Schema , fields, validate , post_load , EXCLUDE , pre_load 

class AppointmentBookSchema(Schema):
    class Meta:
        unknown = EXCLUDE # excluding the unknown field
    name = fields.Str(required=True)
    contact_number = fields.Str(required=True,validate=validate.Length(equal=10))
    age = fields.Int(required=True)

    @post_load
    def serialize_data(self,data,**kwargs):
        return self.dump(data)