from flask_restful import Api
from flask import Blueprint

from system.appointment.AppointmentHandler import AppointmentHandler

appointment = Blueprint("appointment",__name__)

api = Api(appointment)
api.add_resource(AppointmentHandler,"/<int:schedule_id>/")