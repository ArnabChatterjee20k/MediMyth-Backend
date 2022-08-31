import os
class Config:
    SECRET_KEY = "761f9d132273fe311f3e13be9faa56b6"
    PRODUCTION = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:arnab@localhost/medimyth"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
    TWILIO_SERVICE_ID = os.environ.get("TWILIO_SERVICE_ID")