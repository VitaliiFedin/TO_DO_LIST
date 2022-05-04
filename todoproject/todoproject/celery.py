from __future__ import absolute_import, unicode_literals

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoproject.settings')
from celery import Celery
from celery.schedules import crontab
from todoapp.models import Task
from django.utils import timezone
from celery import shared_task
import django

django.setup()
app = Celery('todoproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Creating a celery task
@app.task(bind=True)
def debug_task(self):
    deadline_check = Task.objects.filter(deadline__lte=timezone.now()).exclude(status='Done').update(status='Overdue')
    task_priority_change = Task.objects.filter(status='Done').update(task_priority=0)

