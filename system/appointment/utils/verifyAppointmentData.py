from flask import request
from system.appointment.Schemas.AppointmentBookSchema import AppointmentBookSchema
from marshmallow import ValidationError
from functools import wraps

def verify_appointment(function):
    @wraps(function)
    def inner(*args,**kwargs):
        schema = AppointmentBookSchema()
        data = request.json
        try:
            result = schema.load(data)
            kwargs.update({"update":result})
            return function(*args,**kwargs)
        except ValidationError as error:
            return error.messages , 400
    
    return inner