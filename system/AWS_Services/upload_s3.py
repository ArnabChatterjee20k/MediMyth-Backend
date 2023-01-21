from system.AWS_Services.AWS import AWS
from system.Config import Config
import uuid
import os


def upload_s3(file, name=None):
    service = AWS("s3")
    s3 = service.client
    
    filename = get_image_name(file=file,name=name)
    
    try:
        s3.upload_fileobj(
            file,
            Config.AWS_S3_BUCKET,
            filename,
            ExtraArgs={
                "ContentType": file.content_type  # Set appropriate content type as per the file
            }
        )
    except Exception as e:
        print("Error Happened: ", e)
        return e
    return filename


def get_image_name(file,name=None):
    """For generating unique image name"""
    if name != None:
        return name # name will itself contain the extension
    else:
        file_extension = check_and_get_file_extension(file=file)
        print(file_extension)
        if file_extension == None:
            return None
        return f"{uuid.uuid4()}{file_extension}" # file_extension will itself containing the . so removing the dot


def check_and_get_file_extension(file):
    """Check the file extension if allowed then returns the fie extension"""
    _, f_ext = os.path.splitext(file.filename)
    ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg'}

    if f_ext.lower() not in ALLOWED_EXTENSIONS:
        return None

    return f_ext
