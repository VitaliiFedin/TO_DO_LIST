
from rest_framework import serializers
from django import forms

from .models import Task,TaskCategory
from django.contrib.auth.models import User
from django.db.models import fields


class TaskSerializerAll(serializers.ModelSerializer):

    class Meta:
        model = Task
        deadline = serializers.DateField(format="%Y-%m-%d",input_formats=['%Y-%m-%d',])

        fields = (
              'task_id', 'task_name',  'category', 'task_priority', 'status', 'deadline',
              'time_create', 'time_update')

class TaskSerializer(serializers.ModelSerializer):
    #category = serializers.CharField(source='category.category_name')
    class Meta:
        model = Task
        fields = (
              'task_id', 'task_name', 'time_create', 'deadline',
              )
class SingleTaskSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.category_name')
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Task
        fields = (
            'task_id', 'task_name', 'task_description', 'category', 'task_priority', 'status', 'deadline',
            'time_create', 'time_update','owner')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']