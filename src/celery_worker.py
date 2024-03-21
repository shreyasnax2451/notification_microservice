from celery import Celery
from configs.env import CELERY_REDIS_URL
from services.notifications.interaction.send_notification import send_notification
from kombu import Exchange, Queue

celery = Celery(__name__, 
            broker=CELERY_REDIS_URL, 
            backend=CELERY_REDIS_URL
        )

celery.conf.order_confirmed = [
    Queue(
        'order_confirmed',
        Exchange('order_confirmed'),
        routing_key='order_confirmed',
        queue_arguments={
        'x-max-priority': 2
    }),
]
celery.conf.order_shipped = [
    Queue('order_shipped',
            Exchange('order_shipped'),
            routing_key='order_shipped',
            queue_arguments={
            'x-max-priority': 6
        }),
]
celery.conf.order_out_of_delivery = [
    Queue('order_out_of_delivery',
        Exchange('order_delivery'),
        routing_key='order_delivery',
        queue_arguments={
        'x-max-priority': 6
        }),
]
celery.conf.order_delivered = [
    Queue('order_delivered',
        Exchange('order_delivered'),
        routing_key='order_delivered',
        queue_arguments={
        'x-max-priority': 4
    }),
]
celery.conf.order_returned = [
    Queue('order_returned',
        Exchange('order_returned'),
        routing_key='order_returned',
        queue_arguments={
        'x-max-priority': 4
        }),
]
celery.conf.order_refunded = [
   Queue('order_refunded',
        Exchange('order_refunded'),
        routing_key='order_refunded',
        queue_arguments={
        'x-max-priority': 2
        })
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