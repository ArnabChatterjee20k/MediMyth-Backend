from flask import request
from system.doctor.Schemas.AccountSchema import AccountSchema
from marshmallow import ValidationError
from functools import wraps

def verify_login(function):
    @wraps(function)
    def inner(*args,**kwargs):
        data = request.args
        schema = AccountSchema(only=("email","password"))
        try:
            result = schema.load(data)
            return function(*args,**result)
        except ValidationError as error:
            return error.messages , 400
    
    return inner