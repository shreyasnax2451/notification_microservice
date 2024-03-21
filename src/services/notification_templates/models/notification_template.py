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
    template_type = CharField(index=True)
    template_name = TextField(index=True)
    subject = TextField(null = True)
    template_variables = ArrayField(field_class=TextField, null=True)
    message_template = TextField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
    status = CharField(default = 'active')

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(NotificationTemplate, self).save(*args, **kwargs)

    class Meta:
        table_name = 'notification_templates'
        constraints = [SQL('UNIQUE (template_type, template_name, subject, status)')]