from system.Config import Config
import cloudinary
from cloudinary import uploader , utils
from system.AWS_Services.upload_s3 import get_image_name

class ImageUpload:
    @staticmethod
    def upload_image(file,name):
        cloudinary.config(cloud_name=Config.CLOUDINARY_CLOUD_NAME,api_key=Config.CLOUDINARY_API_KEY,api_secret=Config.CLOUDINARY_API_SECRET)
        filename = get_image_name(file,name)
        file_id = filename.split(".")[0]
        try:
            image = uploader.upload_image(file,filename=filename,public_id=file_id)
        except Exception as e:
            print(e)
        return file_id