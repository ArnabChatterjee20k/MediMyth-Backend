from system.AWS_Services.AWS import AWS
def send_sms(phone_number,message,*args,**kwargs):
    # Create an SNS client
    service = AWS("sns")
    sns = service.client

    # # Send the SMS
    response = sns.publish(
        PhoneNumber=f"+91{phone_number}",
        Message=message
    )
    message_id = response['MessageId']
    return message_id