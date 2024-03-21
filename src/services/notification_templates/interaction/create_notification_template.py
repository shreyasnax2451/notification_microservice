from services.notification_templates.models.notification_template import NotificationTemplate
from database.db_session import db
from operator import attrgetter
from fastapi import HTTPException

def create_notification_template(request):
    with db.atomic():
        return create_notification_template_data(request)

def create_notification_template_data(request):
    query = NotificationTemplate.select()
    for key in request:
        query = query.where(attrgetter(key)(NotificationTemplate) == request.get(key))
    notification_template = query.first()

    if not notification_template:
        notification_template = NotificationTemplate(**request)
    try:
        notification_template.save()
    except Exception:
      raise HTTPException(status_code=500, detail='Notification Template Not Created')

    return {'id': notification_template.id}