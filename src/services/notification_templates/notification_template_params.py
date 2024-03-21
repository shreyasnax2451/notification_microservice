from pydantic import BaseModel

class CreateNotificationTemplate(BaseModel):
  template_type: str
  template_name: str
  template_variables: list[str] = []
  subject: str = None
  message_template: str = None

class UpdateNotificationTemplate(BaseModel):
  id: str
  template_name: str = None
  subject: str = None
  message_template: str = None

class DeleteNotificationTemplate(BaseModel):
  id: str