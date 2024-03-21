from configs.env import *
from services.notifications.helpers.send_email_notification import send_email_notification
from fastapi import HTTPException
from database.db_session import db
from services.notification_templates.interaction.get_notification_template import get_notification_template
from services.notifications.models.notification import Notification

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