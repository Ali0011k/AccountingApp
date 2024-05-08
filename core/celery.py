from celery import Celery
from celery.schedules import crontab
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


app.conf.beat_schedule = {
    # "send_meetings_daily": {
    #     "task": "send_meetings_daily",
    #     "schedule": crontab(hour=7, minute=0),
    # },
}
