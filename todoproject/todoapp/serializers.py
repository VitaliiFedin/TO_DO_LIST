from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task


# Creating serializer for User to retrieve user name
class UserSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'task']


# Creating serializer for Task model to retrieve all fields and convert category into charfield
class TaskSerializerAll(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Task
        fields = '__all__'


# Creating serializer for Task model to retrieve specific fields to show all tasks
class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Task
        fields = (
            'id', 'name', 'time_create', 'deadline', 'author'
        )


# Creating serializer for Task model to retrieve all fields to update purpose
class UpdateTaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Task
        fields = '__all__'
