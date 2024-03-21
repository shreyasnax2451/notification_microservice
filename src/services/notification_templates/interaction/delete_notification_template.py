from services.notification_templates.models.notification_template import NotificationTemplate
from database.db_session import db
from fastapi import HTTPException
from enums.global_enums import Status

def delete_notification_template(request):
    with db.atomic():
        return execute_transaction_code(request)

def execute_transaction_code(request):
    notification_template = NotificationTemplate.select().where(
        NotificationTemplate.id==request.get('id'),
        NotificationTemplate.status == Status.active).first()
    
    if not notification_template:
        raise HTTPException(status_code=404,detail = "Notification Template Not Found")

    notification_template.status = Status.inactive

    try:
        notification_template.save()
    except Exception:
      raise HTTPException(status_code=500, detail='Notification Template did not save')

    return {'id': notification_template.id}