from services.notification_templates.models.notification_template import NotificationTemplate
from database.db_session import db
from enums.global_enums import Status
from fastapi import HTTPException

def update_notification_template(request):
    with db.atomic():
        return execute_transaction_code(request)

def execute_transaction_code(request):
    notification_template = NotificationTemplate.select().where(
        NotificationTemplate.id==request.get('id'),
        NotificationTemplate.status == Status.active).first()
    
    if not notification_template:
        raise HTTPException(status_code=404, detail='Template Not Found')

    for key, value in request.items():
        if value:
            setattr(notification_template, key, value)
    try:
        notification_template.save()
    except:
      raise HTTPException(status_code=500, detail='Template did not update')
    
    return {'id':notification_template.id}