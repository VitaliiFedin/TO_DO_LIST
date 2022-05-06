from django.contrib import admin

from .models import Task, TaskCategory

# Registering models on admin panel.
admin.site.register(Task)
admin.site.register(TaskCategory)
