from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from system.Config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_api():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)
    
    from system.otp import otp
    app.register_blueprint(otp,url_prefix="/otp")

    from system.doctor import doctor
    from system.Models.Doctor import Doctor
    from system.Models.ActiveDoctor import ActiveDoctor
    app.register_blueprint(doctor,url_prefix="/doctor")

    from system.schedule import scheduler
    app.register_blueprint(scheduler,url_prefix="/schedule")

    from system.Models.Appointment import Appointment
    return app