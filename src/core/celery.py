import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")


celery_app = Celery("core")
celery_app.config_from_object(
    obj="django.conf:settings", namespace="CELERY"
)
celery_app.autodiscover_tasks()
celery_app.conf.beat_schedule = {
    "get_news": {
        "task": "news.tasks.get_news",
        "schedule": crontab(hour="*", minute="0")
    },
}
