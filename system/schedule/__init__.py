from flask import Blueprint
from flask_restful import Api

scheduler = Blueprint("scheduler",__name__)
api = Api(scheduler)

from system.schedule.Scheduler import Scheduler
from system.schedule.ScheduleAccess import ScheduleAccess
api.add_resource(Scheduler,"/") ## this for accesing the bulk of schedule
api.add_resource(ScheduleAccess,"/<int:schedule_id>") ## this if for accesing a single schedule