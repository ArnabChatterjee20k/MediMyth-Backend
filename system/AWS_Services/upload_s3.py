from system.AWS_Services.AWS import AWS
from system.Config import Config
import uuid , os
def upload_s3(file):
    service = AWS("s3")
    s3 = service.client
    _ , f_ext = os.path.splitext(file.filename)
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    if f_ext.lower() not in ALLOWED_EXTENSIONS:
        return None
    filename = f"{uuid.uuid4()}.{f_ext}"
    try:
        s3.upload_fileobj(
            file,
            Config.AWS_S3_BUCKET,
            filename,
            ExtraArgs={
                "ContentType": file.content_type    #Set appropriate content type as per the file
            }
        )
    except Exception as e:
        print("Something Happened: ", e)
        return e
    return filename
