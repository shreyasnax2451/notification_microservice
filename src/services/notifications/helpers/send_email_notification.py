import boto3
import re
from fastapi import HTTPException
from configs.env import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION,
    CHARSET,
    SENDER
)

def send_email_notification(request, notification_data):
    try:
        message_content = notification_data['message_template']

        def replace_placeholders(match):
            key = match.group(1)
            return request['notification_data'].get(key, f'<{key} not found>')
        message_content = re.sub('{{(.*?)}}', replace_placeholders, message_content)
        subject = re.sub('{{(.*?)}}', replace_placeholders, notification_data['subject'])

        RECIPIENT = request['email_address']
        SUBJECT = subject
        BODY_TEXT = ("Notification AWS Test\r\n"
                    "This notification was sent with Amazon SES using the "
                    "AWS SDK for Python (Boto)."
                    ) 
        BODY_HTML = message_content
        session = boto3.Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
        client = session.client('ses',region_name=AWS_REGION)
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)