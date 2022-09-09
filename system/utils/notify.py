
from twilio.rest import Client
from system.Config import Config
import json
from system import celery
# To set up environmental variables, see http://twil.io/secure
ACCOUNT_SID = Config.TWILIO_ACCOUNT_SID
AUTH_TOKEN = Config.TWILIO_AUTH_TOKEN

client = Client(ACCOUNT_SID, AUTH_TOKEN)

@celery.task
def send_bulk_sms(numbers:list, body:str,*args,**kwargs):
    bindings = list(map(lambda number: json.dumps({'binding_type': 'sms', 'address': number.get("contact_number")}), numbers))
    print("=====> To Bindings :>", bindings, "<: =====")
    notification = client.notify.services("MG0e9c714b83d28bf91be07c522e874e10").notifications.create(
        to_binding=bindings,
        body=body
    )
    print(notification.body)