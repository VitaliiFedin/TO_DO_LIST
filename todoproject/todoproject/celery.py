from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

from .schedule import beat_schedule

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoproject.settings')
app = Celery('todoproject')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
app.conf.beat_schedule = beat_schedule
# import django


# django.setup()

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.

# Load task modules from all registered Django app configs.


# Creating a celery task
# @app.task(bind=True)
# def debug_task(self):
#     deadline_check = Task.objects.filter(deadline__lte=timezone.now()).exclude(status='Done').update(status='Overdue')
#     task_priority_change = Task.objects.filter(status='Done').update(task_priority=0)
