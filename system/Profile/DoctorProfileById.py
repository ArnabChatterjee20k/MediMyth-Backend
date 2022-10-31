from flask import jsonify , make_response
from flask_restful import Resource
from system.Models.ActiveDoctor import ActiveDoctor
from system.Models.Doctor import Doctor
from system.Models.DoctorDetailsVisibility import DoctorDetailsVisibility
from system.Profile.Schemas.Doctor.ProfileByIdSchema import ProfileByIdSchema
class DoctorProfileById(Resource):
    def get(self,id,*args,**kwargs):
        doctor = Doctor.query.join(ActiveDoctor).filter(ActiveDoctor.id == id)
        doctor_present = doctor.first_or_404()
        fields_to_be_excluded = ["_password"]
        visibility_details = doctor_present.details_visible.first()
        details = ("email","reg_no","phone_no")
        for detail in details:
            if(getattr(visibility_details,detail)==False):
                fields_to_be_excluded.append(detail)

        profile = ProfileByIdSchema(exclude=tuple(fields_to_be_excluded))
        return profile.dump(doctor.all(),many=True)
                
        