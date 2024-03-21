from pydantic import BaseModel

class SendNotification(BaseModel):
  template_data: dict = {}
  notification_data: dict = {}
  email_address: str
  user_id: str