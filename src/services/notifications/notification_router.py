from fastapi import APIRouter, HTTPException
from services.notifications.interaction.send_notification import send_notification
from celery_worker import send_notification_delay
from libs.json_encoder import json_encoder
from services.notifications.notification_params import *
from fastapi.responses import JSONResponse
from logger import logging

notification_router = APIRouter()

@notification_router.post("/send_notification")
def send_notification_api(request: SendNotification):
    try:
        send_notification_delay.apply_async(kwargs = {'request':request.dict()}, queue = 'communication')
        return JSONResponse(status_code=200, content={'success' : True})
    except HTTPException as e:
        raise
    except Exception as e:
        logging.info(e)
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })