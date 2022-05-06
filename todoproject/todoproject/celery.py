from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

from .schedule import beat_schedule

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoproject.settings')
app = Celery('todoproject')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
app.conf.beat_schedule = beat_schedule

