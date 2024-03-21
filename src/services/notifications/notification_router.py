from fastapi import APIRouter, HTTPException
from services.notifications.interaction.send_notification import send_notification
from libs.json_encoder import json_encoder
from services.notifications.notification_params import *
from fastapi.responses import JSONResponse

notification_router = APIRouter()

@notification_router.post("/send_notification")
def send_notification_api(request: SendNotification):
    try:
        data = send_notification(request.dict())
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })