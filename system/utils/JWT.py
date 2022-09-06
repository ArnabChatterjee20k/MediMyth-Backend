from itsdangerous import URLSafeSerializer
from system.Config import Config
from flask import request , make_response
from functools import wraps
serializer = URLSafeSerializer(Config.SECRET_KEY)
def generate_jwt(data):
    return serializer.dumps(data)

def verify_jwt(data):
    return serializer.loads(data)

def token_required(function):
    @wraps(function)
    def inner(*args,**kwargs):
        # print("jwt",kwargs)
        token = request.headers.get("access-token")
        if token:
            try:
                data = verify_jwt(token)
            except Exception as e:
                print(e)

                # if data is passed to kwargs from another function then we should accept that and also send that data
                # token containing some data like email which may be also present in the kwargs
                # here if extra data comes from the previous function then that data comes through kwargs. 
                # **data and **kwargs will get merged into a single dictionary automatically as function can accept only one **kwargs but if we pass multiple then all of them get merged into one
                return make_response({Config.RESPONSE_KEY:"invalid access token"},400)
            return function(*args,**data,**kwargs) # both the data from kwargs and from this function 
        return make_response({Config.RESPONSE_KEY:"access-token not found"},404)
    return inner