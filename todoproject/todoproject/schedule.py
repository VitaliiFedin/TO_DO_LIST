from celery.schedules import crontab

beat_schedule = {
    'add-daily at midnight': {
        'task': 'todoapp.task.debug_task',
        'schedule': crontab(),
        'options': {
            'expires': 15.0,
        },
    },
}

# CELERY_BEAT_SCHEDULE = {
#     'add-daily at midnight': {
#         'task': 'todoproject.celery.debug_task',
#         'schedule': crontab(),
#         'options': {
#             'expires': 15.0,
#         },
#     },
# }
