from flask import request, abort
from flask_restful import Resource
from system.utils.JWT import token_required
from system.Config import Config
from system.Models.ActiveDoctor import ActiveDoctor
from system.Models.Doctor import Doctor
from system.ImageUploadServices.ImageUpload import ImageUpload
from system import db
from system.AWS_Services.upload_s3 import upload_s3


class UploadPicture(Resource):
    @token_required
    def put(self, **data):
        file = request.files.get("image")
        if file is None:
            return {Config.RESPONSE_KEY: "Please select a file"}, 403
        email = data.get("email")
        doctor = Doctor.query.join(ActiveDoctor).filter(
            Doctor.email == email).first_or_404()
        doctor_profile_pic_exists = doctor.profile_pic
        filename = ImageUpload.upload_image(file, name=doctor_profile_pic_exists)
        print(filename , doctor_profile_pic_exists)
        if filename == None:
            return {Config.RESPONSE_KEY: "File Format Not Supported"}, 403
        doctor.profile_pic = filename
        db.session.commit()
        return {Config.RESPONSE_KEY: "Success"}, 200