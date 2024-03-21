from fastapi import FastAPI, Depends
from configs.env import *
from services.notifications.notification_router import notification_router
from services.notification_templates.notification_template_router import notification_template_router
from database.db_support import get_db

app = FastAPI()

app.include_router(prefix = "/notification", router=notification_router, tags=['Notification'], dependencies=[Depends(get_db)])
app.include_router(prefix = "/notification_template", router = notification_template_router, tags=['Notification Template'], dependencies=[Depends(get_db)])

@app.get("/")
def read_root():
    return "Welcome To Notification Microservice"