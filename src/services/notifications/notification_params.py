from pydantic import BaseModel

class SendNotification(BaseModel):
  template_data: dict = {}
  notification_data: dict = {}
  user_id: str