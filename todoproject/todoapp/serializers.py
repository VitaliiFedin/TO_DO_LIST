from rest_framework import serializers
from django import forms
from .models import Task, TaskCategory
from django.contrib.auth.models import User


# Creating serializer for User to retrieve user name
class UserSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'task']


# Creating serializer for Task model to retrieve all fields and convert category into charfield
class TaskSerializerAll(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = serializers.CharField(source='category.category_name')

    class Meta:
        model = Task
        author = serializers.ReadOnlyField(source='author.username')
        fields = (
            'task_id', 'task_name', 'task_description', 'category', 'task_priority', 'status', 'deadline',
            'time_create', 'time_update', 'author')


# Creating serializer for Task model to retrieve specific fields to show all tasks
class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Task
        fields = (
            'task_id', 'task_name', 'time_create', 'deadline', 'author'
        )


# Creating serializer for Task model to retrieve all fields to update purpose
class UpdateTaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Task
        fields = (
            'task_id', 'task_name', 'task_description', 'category', 'task_priority', 'status', 'deadline',
            'time_create', 'time_update', 'author')
