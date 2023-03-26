from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from system.Config import Config
from celery import Celery
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
print(__name__)
celery = Celery(__name__,broker=Config.broker_url, result_backend=Config.result_backend)

def create_api():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    db.init_app(app)
    celery.conf.update(app.config)
    migrate.init_app(app,db)
        
    from system.otp import otp
    app.register_blueprint(otp,url_prefix="/otp")

    from system.doctor import doctor
    from system.Models.Doctor import Doctor
    from system.Models.ActiveDoctor import ActiveDoctor
    app.register_blueprint(doctor,url_prefix="/doctor")

    from system.Vacation import vacation
    from system.Models.ScheduleVacation import schedule_vacation
    from system.Models.Vacation import Vacation
    app.register_blueprint(vacation,url_prefix="/vacation")

    from system.Profile import profile
    app.register_blueprint(profile,url_prefix="/profiles")

    from system.schedule import scheduler
    app.register_blueprint(scheduler,url_prefix="/schedule")

    from system.Models.Appointment import Appointment
    from system.appointment import appointment
    app.register_blueprint(appointment,url_prefix="/appointment")


    from system.category import category
    from system.Models.Category import Category
    app.register_blueprint(category,url_prefix="/category")

    from system.admin import doctor_handler
    app.register_blueprint(doctor_handler,url_prefix="/admin")
    
    return app