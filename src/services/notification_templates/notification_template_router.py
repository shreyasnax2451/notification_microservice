from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from services.notification_templates.notification_template_params import *
from libs.json_encoder import json_encoder

from services.notification_templates.interaction.create_notification_template import create_notification_template
from services.notification_templates.interaction.get_notification_template import get_notification_template
from services.notification_templates.interaction.update_notification_template import update_notification_template
from services.notification_templates.interaction.delete_notification_template import delete_notification_template

notification_template_router = APIRouter()

@notification_template_router.post('/create_notification_template')
def create_notification_template_api(request: CreateNotificationTemplate):
    try:
        create_template = create_notification_template(request.dict())
        return JSONResponse(status_code=200,content=json_encoder(create_template))
    except HTTPException as e :
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })

@notification_template_router.post('/delete_notification_template')
def delete_notification_template_api(request: DeleteNotificationTemplate):
    try:
        delete_template = delete_notification_template(request.dict())
        return JSONResponse(status_code=200,content=json_encoder(delete_template))
    except HTTPException as e :
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })

@notification_template_router.post("/update_notification_template")
def update_notification_template_api(request: UpdateNotificationTemplate):
    try:
        data = update_notification_template(request.dict())
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })

@notification_template_router.get("/get_notification_template")
def get_notification_template_api(
    template_type: str = None,
    template_name: str = None,
    status: str = None,
):
    try:
        request = {
            'template_type':template_type,
            'template_name':template_name,
            'status':status
        }
        data = get_notification_template(request)
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })