from peewee import *
import datetime
from database.db_session import db
from playhouse.postgres_ext import BinaryJSONField
from services.notification_templates.models.notification_template import NotificationTemplate
class BaseModel(Model):
    class Meta:
        database = db
        only_save_dirty = True

class Notification(BaseModel):
    id = UUIDField(constraints=[SQL("DEFAULT gen_random_uuid()")], index=True, primary_key = True)
    notification_data = BinaryJSONField(null=True)
    user_id = UUIDField(index = True)
    notification_template_id = ForeignKeyField(NotificationTemplate,to_field="id")
    created_at = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        self.created_at = datetime.datetime.now()
        return super(Notification, self).save(*args, **kwargs)

    class Meta:
        table_name = 'notifications'