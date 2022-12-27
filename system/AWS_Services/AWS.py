from system.Config import Config
import boto3

class AWS:
    region_name = Config.AWS_REGION
    aws_access_key_id = Config.AWS_ACCESS_KEY_ID
    aws_secret_access_key = Config.AWS_SECRET_ACCESS_KEY
    def __init__(self,service):
        self.client = boto3.client(service,region_name=self.region_name,aws_access_key_id=self.aws_access_key_id,aws_secret_access_key=self.aws_secret_access_key)