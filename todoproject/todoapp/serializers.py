from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task


class UserSerializer(serializers.ModelSerializer):
    """
    This class uses for converting  user model fields data in JSON

    """
    task = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'task']



class TaskSerializerAll(serializers.ModelSerializer):
    """
        This class uses for converting  task model fields data in JSON

    """
    author = serializers.ReadOnlyField(source='author.username')
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Task
        fields = '__all__'


# Creating serializer for Task model to retrieve specific fields to show all tasks
class TaskSerializer(serializers.ModelSerializer):
    """
        This class uses for converting specific task model fields data in JSON

    """
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Task
        fields = (
            'id', 'name', 'time_create', 'deadline', 'author'
        )


# Creating serializer for Task model to retrieve all fields to update purpose
class UpdateTaskSerializer(serializers.ModelSerializer):
    """
        This class uses for converting  task model fields data in JSON

    """

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Task
        fields = '__all__'
