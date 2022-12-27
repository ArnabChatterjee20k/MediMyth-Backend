from system import celery
from datetime import date
from system.AWS_Services.send_sms import send_sms
@celery.task
def deleted_schedule(name,phone,appointment_date,appointment_id,*args,**kwargs):
    format_date = date.strftime(appointment_date,r"%d/%m/%Y")
    message = f"Sorry {name}, your appointment on {format_date} of {appointment_id} is cancelled."
    send_sms(phone_number=phone,message=message)