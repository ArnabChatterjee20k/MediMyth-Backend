from flask_restful import Resource

class AppointmentHandler(Resource):
    def get(self):
        return "done"