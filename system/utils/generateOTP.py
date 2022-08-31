from twilio.rest import Client
from system.Config import Config
def send_sms(phone):

    account_sid = Config.TWILIO_ACCOUNT_SID
    auth_token = Config.TWILIO_AUTH_TOKEN
    servide_id = Config.TWILIO_SERVICE_ID

    client = Client(account_sid,auth_token)
    message = client.verify.v2.services(servide_id).verifications.create(
        to=f"+91{phone}",
        channel = "sms"
    )
    print(message.status)
    return message.status