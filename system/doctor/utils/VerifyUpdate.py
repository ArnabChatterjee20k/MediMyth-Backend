from system.doctor.Schemas.AccountSchema import AccountSchema
from functools import wraps
from flask import request
from marshmallow import ValidationError

def verify_update(function):
    @wraps(function)
    def inner(*args,**kwargs):
        data = request.json
        schema = AccountSchema(partial=True)
        try:
            result = schema.load(data)
            return function(*args,**result)
        except ValidationError as error:
            return error.messages , 400
    
    return inner
