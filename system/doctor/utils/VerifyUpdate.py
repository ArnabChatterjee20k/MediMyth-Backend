from system.doctor.Schemas.AccountSchema import AccountSchema
from functools import wraps
from flask import request
from marshmallow import ValidationError

def verify_update(function):
    @wraps(function)
    def inner(*args,**kwargs):
        data = request.json
        schema = AccountSchema(partial=True,exclude=("password",))
        try:
            result = schema.load(data)
            kwargs.update({"update":result})
            return function(*args,**kwargs)
        except ValidationError as error:
            return error.messages , 400
    
    return inner
