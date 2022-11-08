from flask_restful import Resource
from system.Models.ActiveDoctor import ActiveDoctor
from system.Models.Doctor import Doctor
from system.Profile.Schemas.Doctor.ProfileByEmailSchema import ProfileByEmailSchema
from system.utils.JWT import token_required
class DoctorProfileByEmail(Resource):
    @token_required
    def get(self,*args,**kwargs):
        email = kwargs.get("email")
        doctor = Doctor.query.join(ActiveDoctor).filter(Doctor.email==email)
        doctor.first_or_404()
        profile = ProfileByEmailSchema()
        return profile.dump(doctor.all(),many=True)