from twilio.rest import Client
from system.Config import Config
def send_sms(phone):

    account_sid = Config.TWILIO_ACCOUNT_SID
    auth_token = Config.TWILIO_AUTH_TOKEN
    client = Client(account_sid,auth_token)
    message = client.verify.v2.services("VA5d7b059dcd559f4a0fa2c6423f971bdb").verifications.create(
        to=f"+91{phone}",
        channel = "sms"
    )
    print(message.status)
    return message.status