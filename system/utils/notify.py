
import os
from twilio.rest import Client
from system.Config import Config
import json
from system import celery
# To set up environmental variables, see http://twil.io/secure
ACCOUNT_SID = Config.TWILIO_ACCOUNT_SID
AUTH_TOKEN = Config.TWILIO_AUTH_TOKEN

client = Client(ACCOUNT_SID, AUTH_TOKEN)
notify_sid = os.environ.get("TWILIO_NOTIFY_SID")
@celery.task
def send_bulk_sms(numbers:list, body:str,*args,**kwargs):
    bindings = list(map(lambda number: json.dumps({'binding_type': 'sms', 'address': number.get("contact_number")}), numbers))
    print("=====> To Bindings :>", bindings, "<: =====")
    notification = client.notify.services(notify_sid).notifications.create(
        to_binding=bindings,
        body=body
    )
    print(notification.body)