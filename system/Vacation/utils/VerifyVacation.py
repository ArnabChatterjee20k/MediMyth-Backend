from flask import request
from system.Vacation.Schema.VacationCreationSchema import VacationCreationSchema
from marshmallow import ValidationError
from functools import wraps

def verify_vacation(function):
    @wraps(function)
    def inner(*args,**kwargs):
        data = request.json
        schema = VacationCreationSchema()
        try:
            result = schema.load(data)    
            kwargs.update({"update":result})
            return function(*args,**kwargs)
        except ValidationError as error:
            return error.messages , 400
    
    return inner
