from flask import Blueprint
from flask_restful import Api

scheduler = Blueprint("scheduler",__name__)
api = Api(scheduler)

from system.schedule.Scheduler import Scheduler
api.add_resource(Scheduler,"/")