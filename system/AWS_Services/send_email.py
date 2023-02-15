from system.AWS_Services.AWS import AWS
from system import celery

@celery.task
def send_email(recipient, sender, subject, body):
    service = AWS("ses")
    ses = service.client

    if not recipient or not sender or not subject or not body:
        raise Exception("Parameters missing")

    def use_temaplate():
        return {
            'Subject': {
                'Data': subject
            },
            'Body': {
                'Text': {
                    'Data': body
                }
            }
        }

    response = ses.send_email(
        Source=sender,
        Destination={
            'ToAddresses': [
                recipient
            ]
        },
        Message=use_temaplate()
    )

    print(response)
