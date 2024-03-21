from peewee import *
import datetime
from database.db_session import db
from playhouse.postgres_ext import ArrayField
class BaseModel(Model):
    class Meta:
        database = db
        only_save_dirty = True

class NotificationTemplate(BaseModel):
    id = UUIDField(constraints=[SQL("DEFAULT gen_random_uuid()")], index=True, primary_key = True)
    type = CharField(index=True)
    name = TextField(index=True)
    subject = TextField(index=True)
    variables = ArrayField(field_class=TextField, null=True)
    content = TextField(index=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
    html_template = TextField(null=True)
    status = CharField(default = 'active')
    # notification_event_id =

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(NotificationTemplate, self).save(*args, **kwargs)

    class Meta:
        table_name = 'notification_templates'