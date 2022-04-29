from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework import serializers
from rest_framework import status
from datetime import datetime
from .models import *

@api_view(['GET'])
def TaskOverview(request):
    api_urls = {
        'All tasks': '/all',
        'Single task': '/task/pk',
        # 'Search by Category': '/?category=category_name',
        # 'Search by Subcategory': '/?subcategory=category_name',
        'Create': '/create',
        'Update': '/update/pk',
        'Delete': '/task/delete/pk'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_tasks(request):
    task = TaskSerializer(data=request.data)

    if Task.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if task.is_valid():
        task.save()
        return Response(task.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_tasks(request):
    # tasks = Task.objects.all()
    # serializer = TaskSerializer(tasks,many=True)
    if request.query_params:
        tasks = Task.objects.filter(**request.query_param.dict())
    else:
        # tasks = Task.objects.all().order_by("-task_priority")
        tasks = Task.objects.all().order_by("task_priority")
    if tasks:
        # data = TaskSerializer(tasks)
        return Response(TaskSerializer(tasks, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    data = TaskSerializer(instance=task, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_tasks(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def view_task(request, pk):
    tasks = Task.objects.get(pk=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)
