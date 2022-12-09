from flask_restful import Resource
from flask import make_response,jsonify
from system.Config import Config
from system.Models.Vacation import Vacation
from system.Models.ActiveDoctor import ActiveDoctor
from system.Models.Doctor import Doctor
from system.utils.JWT import token_required
from system.Vacation.Schema.VacationSchema import VacationSchema
from system.Vacation.utils.VerifyVacation import verify_vacation
class VacationHandler(Resource):
    @token_required
    def get(self,**data):
        email = data.get("email")
        vacations = Vacation.query.join(ActiveDoctor,Doctor).filter(Doctor.email==email).all()
        schema = VacationSchema()
        return make_response(jsonify(schema.dump(vacations,many=True)))

    @verify_vacation
    @token_required
    def post(self,**data):
        email = data.get("email")
        vacation_details = data.get("update")
        try:
            doctor = ActiveDoctor.query.join(Doctor).filter(Doctor.email==email).first_or_404()
        except:
            return make_response({Config.RESPONSE_KEY:"doctor not found"},404)
        doctor_id = doctor.id
        exist = Vacation.vacation_exist(active_doctor_id=doctor_id,**vacation_details)
        if(exist):
            return make_response({Config.RESPONSE_KEY:"vacation exist"},403)
        Vacation.create_vacation(active_doctor_id=doctor_id,**vacation_details)