from pydantic import BaseModel

class CreateNotificationTemplate(BaseModel):
  type: str
  name: str
  variables: list[str] = []
  subject: str
  content: str = None
  html_template: str = None

class UpdateNotificationTemplate(BaseModel):
  id: str
  name: str = None
  subject: str = None
  html_template: str = None

class DeleteNotificationTemplate(BaseModel):
  id: str