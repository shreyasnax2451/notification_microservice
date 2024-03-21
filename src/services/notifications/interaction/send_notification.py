from configs.env import *
import smtplib
from fastapi import HTTPException
from database.db_session import db
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from services.notification_templates.interaction.get_notification_template import get_notification_template
from services.notifications.models.notification import Notification

def send_email_notification(request):
    notification_data = get_notification_template({
        'type':request['template_data']['type'],
        'name':request['template_data']['name']
    })
    html_content = notification_data['html_template']
    for key in request['notification_data']:
        html_content = html_content.replace(f'{key}', request['notification_data'].get(key))
    try:
        sender_email = EMAIL_ADDRESS_SMPT
        recipient_email = EMAIL_ADDRESS_SMPT
        password = PASSWORD_SMPT

        message = MIMEMultipart("alternative")
        message["Subject"] = notification_data['subject']
        message["From"] = sender_email
        message["To"] = recipient_email

        html_part = MIMEText(html_content, "html")
        message.attach(html_part)

        with smtplib.SMTP("smtp.gmail.com", "587") as connection:
            # server.login(sender_email, password)
            # server.sendmail(sender_email, recipient_email, message.as_string())
            connection.starttls()
            connection.login(user = sender_email, password = password)
            connection.sendmail(
                from_addr = sender_email, 
                to_addrs = recipient_email, 
                msg = message.as_string()
            )
        return True
    except Exception as e:
        print(e)
        print('Email Failed!')
    
def send_notification(request):
    with db.atomic():
        if send_email_notification(request):
            notification_data = request['notification_data'] | request['template_data']
            notification = Notification.create(
                notification_data = notification_data,
                user_id = request['user_id']
            )
            return notification.id
        else:
            raise HTTPException(status_code=500, detail='Notification Not Sent')