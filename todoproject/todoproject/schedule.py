from celery.schedules import crontab
# Creating a schedule to perform a celery task.
beat_schedule = {
    'add-daily at midnight': {
        'task': 'todoapp.task.debug_task',
        'schedule': crontab(minute=0, hour=0),
        'options': {
            'expires': 15.0,
        },
    },
}

