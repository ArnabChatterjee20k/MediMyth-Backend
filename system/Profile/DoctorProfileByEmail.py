from flask_restful import Resource
from system.Models.ActiveDoctor import ActiveDoctor
from system.Models.Doctor import Doctor
from system.Profile.Schemas.Doctor.ProfileByEmailSchema import ProfileByEmailSchema

class DoctorProfileByEmail(Resource):
    def get(self,email,*args,**kwargs):
        doctor = Doctor.query.join(ActiveDoctor).filter(Doctor.email==email)
        doctor.first_or_404()
        profile = ProfileByEmailSchema()
        return profile.dump(doctor.all(),many=True)