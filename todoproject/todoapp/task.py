#from datetime import timezone
from django.utils import timezone
from celery import shared_task

from .models import Task


# import django
#
# django.setup()



@shared_task
def debug_task():
    deadline_check = Task.objects.filter(deadline__lte=timezone.now()).exclude(status='Done').update(status='Overdue')
    task_priority_change = Task.objects.filter(status='Done').update(priority=0)
