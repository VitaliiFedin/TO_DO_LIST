#from datetime import timezone
from celery import shared_task
from django.utils import timezone

from .models import Task


@shared_task
def debug_task():
    """
    This function filters the records by deadline and status and change the status and priority values

    """
    deadline_check = Task.objects.filter(deadline__lte=timezone.now()).exclude(status='Done').update(status='Overdue')
    task_priority_change = Task.objects.filter(status='Done').update(priority=0)
