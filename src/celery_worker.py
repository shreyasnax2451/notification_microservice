from celery import Celery
from services.notifications.interaction.send_notification import send_notification

celery = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
from kombu import Exchange, Queue

celery.conf.communication_queues = [
    Queue(
        "communication",
        Exchange("communication"),
        routing_key="communication",
        queue_arguments={"x-max-priority": 6},
    )
]

@celery.task(bind=True, retry_backoff=True, max_retries=1)
def send_notification_delay(self, request):
    try:
        send_notification(request)
    except Exception as exc:
        if type(exc).__name__ == "HTTPException":
            pass
        else:
            raise self.retry(exc=exc)