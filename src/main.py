from fastapi import FastAPI, Depends
from configs.env import *
from database.db_session import db
from services.notifications.notification_router import notification_router
from services.notification_templates.notification_template_router import notification_template_router
from database.db_support import get_db

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(prefix = "/notification", router=notification_router, tags=['Notification'], dependencies=[Depends(get_db)])
app.include_router(prefix = "/notification_template", router = notification_template_router, tags=['Notification Template'], dependencies=[Depends(get_db)])

@app.get("/")
def read_root():
    return "Welcome To Notification Microservice"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    if db.is_closed():
        db.connect()

@app.on_event("shutdown")
def shutdown():
    if not db.is_closed():
        db.close()