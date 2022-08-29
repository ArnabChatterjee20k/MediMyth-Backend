import os
class Config:
    SECRET_KEY = "761f9d132273fe311f3e13be9faa56b6"
    PRODUCTION = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:arnab@localhost/medimyth"
    SQLALCHEMY_TRACK_MODIFICATIONS = True