# celery.py
from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab # scheduler
# default django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','finance.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = Celery('scraper')
app.conf.timezone = 'UTC'
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.beat_schedule = {
    # executes every 1 minute
    'scraping-task-one-min': {
        'task': 'scraper.tasks.start_scraping',
        'schedule': crontab()
    }
}