from django.contrib import admin
from .models import Task, TaskCategory

# Register your models here.
admin.site.register(Task)
admin.site.register(TaskCategory)
