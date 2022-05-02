from rest_framework import serializers
from .models import Task,TaskCategory

from django.db.models import fields


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
              'task_id', 'task_name', 'task_description', 'category', 'task_priority', 'status', 'deadline',
              'time_create', 'time_update')

class TaskSerializernormal(serializers.ModelSerializer):
    category = serializers.CharField(source='category.category_name')
    class Meta:
        model = Task
        fields = (
              'task_id', 'task_name', 'task_description', 'category', 'task_priority', 'status', 'deadline',
              'time_create', 'time_update')


