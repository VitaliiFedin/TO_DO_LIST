from rest_framework import serializers
from .models import Task
from django.db.models import fields


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'task_id', 'task_name', 'task_description', 'category', 'task_priority', 'status', 'deadline',
            'time_create', 'time_update')
