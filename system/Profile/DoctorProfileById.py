from flask import jsonify , make_response
from flask_restful import Resource
from system.Models.ActiveDoctor import ActiveDoctor
from system.Models.Doctor import Doctor
from system.Profile.Schemas.Doctor.ProfileByIdSchema import ProfileByIdSchema
class DoctorProfileById(Resource):
    def get(self,id,*args,**kwargs):
        doctor = Doctor.query.join(ActiveDoctor).filter(ActiveDoctor.id == id)
        doctor_present = doctor.first_or_404()
        fields_to_be_excluded = ["_password"]
        details = {
            "email_visibility":"email",
            "reg_no_visibility":"reg_no",
            "phone_no_visibility":"phone_no"
            }
        for detail in details:
            if(getattr(doctor_present,detail)==False):
                fields_to_be_excluded.append(details.get(detail))

        profile = ProfileByIdSchema(exclude=tuple(fields_to_be_excluded))
        return profile.dump(doctor.all(),many=True)
                
        