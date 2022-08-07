from django.utils.timezone import datetime

from core.celery import celery_app
from .services import FinhubService, CustomDatesFinhubService


@celery_app.task
def get_news():
    FinhubService().get_news()
    

@celery_app.task
def get_news_in_range(from_date=None, to_date=None):
    CustomDatesFinhubService(
        from_date=from_date,
        to_date=to_date,
    ).get_news()
