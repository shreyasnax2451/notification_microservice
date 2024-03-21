from configs.env import *
import re
import boto3
from fastapi import HTTPException
from database.db_session import db
from services.notification_templates.interaction.get_notification_template import get_notification_template
from services.notifications.models.notification import Notification

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
    
def send_notification(request):
    notification_template_data = get_notification_template({
        'template_type':request['template_data']['template_type'],
        'template_name':request['template_data']['template_name']
    })
    if notification_template_data:
        with db.atomic():
            if send_email_notification(request, notification_template_data):
                notification_data = request['notification_data'] | request['template_data']
                notification = Notification.create(
                    notification_data = notification_data,
                    user_id = request['user_id'],
                    notification_template_id = notification_template_data['id']
                )
                return {"id":notification.id}
    else:
        raise HTTPException(status_code=404, detail='Template Not Found')