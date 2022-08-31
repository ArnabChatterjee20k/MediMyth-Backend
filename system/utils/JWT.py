from itsdangerous import URLSafeSerializer
from system.Config import Config
from flask import request , abort
from functools import wraps
serializer = URLSafeSerializer(Config.SECRET_KEY)
def generate_jwt(data):
    return serializer.dumps(data)

def verify_jwt(data):
    return serializer.loads(data)