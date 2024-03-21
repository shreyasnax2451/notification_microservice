from services.notification_templates.models.notification_template import NotificationTemplate
from operator import attrgetter
from playhouse.shortcuts import model_to_dict

def get_notification_template(request):
    response = {}
    if all(value for value in request.values()):
          query = NotificationTemplate.select()
          for key in request:
                query = query.where(attrgetter(key)(NotificationTemplate) == request.get(key))
          response = query.first()
          if response:
               response = model_to_dict(response)     

    return response