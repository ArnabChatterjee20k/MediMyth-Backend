from flask import request
from system.schedule.Schemas.ScheduleSchema import ScheduleSchema
from functools import wraps
from marshmallow import ValidationError
def verify_schedule(function):
    def inner(*args,**kwargs):
        schema = ScheduleSchema()
        data = request.json
        try:
            result = schema.load(data)
        except ValidationError as error:
            return error.messages , 400
        return function(*args,**result)
    return inner
