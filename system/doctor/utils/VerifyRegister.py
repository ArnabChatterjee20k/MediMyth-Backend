from flask import request
from system.utils.verifyOTP import check
from system.doctor.Schemas.AccountSchema import AccountSchema
from marshmallow import ValidationError
from functools import wraps

def verify_register(function):
    @wraps(function)
    def inner(*args,**kwargs):
        schema = AccountSchema()
        data = request.json
        try:
            result = schema.load(data)
            kwargs.update({"update":result})
            return function(*args,**kwargs)
        except ValidationError as error:
            return error.messages , 400
    
    return inner