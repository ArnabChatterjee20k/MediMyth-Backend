from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from system.Config import Config

db = SQLAlchemy()

def create_api():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from system.otp import otp
    app.register_blueprint(otp,url_prefix="/otp")

    from system.doctor import doctor
    app.register_blueprint(doctor,url_prefix="/doctor")
    return app