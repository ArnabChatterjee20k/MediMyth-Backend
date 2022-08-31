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
        token = request.headers.get("access-token")
        if token:
            try:
                data = verify_jwt(token)
            except Exception as e:
                print(e)
                
                # if data is passed to kwargs from another function then we should accept that and also send that data
                # token containing some data like email which may be also present in the kwargs
                return make_response({"status":"invalid access token"},400)
            data.update({"update":kwargs}) #update returns none
            return function(*args,**data)
        return make_response({"status":"access-token not found"},404)
    return inner