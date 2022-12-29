import os
class Config:
    SECRET_KEY = "761f9d132273fe311f3e13be9faa56b6"
    PRODUCTION = False
    DEBUG = not PRODUCTION
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:arnab@localhost/medimyth"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID") or "none"
    TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN") or "none"
    TWILIO_SERVICE_ID = os.environ.get("TWILIO_SERVICE_ID") or "none"
    
    broker_url = os.environ.get("redis_config")
    result_backend = os.environ.get("redis_config")
    
    ALGOLIA_APP_ID = os.environ.get("ALGOLIA_APP_ID")
    ALOGOLIA_API_KEY_ADMIN = os.environ.get("ALOGOLIA_API_KEY_ADMIN")
    
    AWS_REGION = os.environ.get("AWS_REGION")
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_BUCKET = "mmdoctorbucket"

    RESPONSE_KEY = "status"
    DOCTOR_TAG = "MM"
    UTC_String_Format = r"%Y-%m-%d" # will be accepting utc string 