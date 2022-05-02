from django.shortcuts import render
import os
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from todoproject.celery import debug_task
from .models import Task as ClassTask
from .serializers import TaskSerializer
from .serializers import TaskSerializernormal
from rest_framework import serializers
from rest_framework import status
from celery import *
from django.utils import timezone


#debug_task.apply_async(utc=datetime(2022,5,2,15,22))

@api_view(['GET'])
def TaskOverview(request):
    api_urls = {
        'All tasks': '/all',
        'Single task': '/task/pk',
        'Create': '/create',
        'Update': '/update/pk',
        'Delete': '/task/delete/pk',
        'Overdue': 'task/overdue/'
    }
    # deadline_check = Task.objects.filter(
    #     deadline__lte=timezone.now()).exclude(status='Done').update(status='Overdue')
    #debug_task()
    #debug_task.delay()

    return Response(api_urls)


@api_view(['POST'])
def add_tasks(request):
    task = TaskSerializer(data=request.data)
    if ClassTask.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if task.is_valid():
        task.save()
        #debug_task.delay()
        return Response(task.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_tasks(request):
    if request.query_params:
        tasks = ClassTask.objects.filter(**request.query_param.dict())
    else:
        tasks = ClassTask.objects.all().order_by("-status", 'task_priority')
    if tasks:
        #debug_task.delay()
        return Response(TaskSerializernormal(tasks, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_task(request, pk):
    task = ClassTask.objects.get(pk=pk)
    data = TaskSerializer(task, data=request.data, partial=True)
    data_view=TaskSerializernormal(task,many=False)
    if data.is_valid():
        data.save()
        #debug_task.delay()
        return Response(data_view.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_tasks(request, pk):
    task = get_object_or_404(ClassTask, pk=pk)
    task.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def view_task(request, pk):
    tasks = ClassTask.objects.get(pk=pk)
    serializer = TaskSerializernormal(tasks, many=False)
    #debug_task.delay()
    # deadline_check = Task.objects.filter(
    #     deadline__lte=timezone.now()).exclude(status='Done').update(status='Overdue')
    return Response(serializer.data)


@api_view(['GET'])
def overdue_tasks(request):
    if request.query_params:
        tasks =ClassTask.objects.filter(**request.query_param.dict())
    else:
        tasks = ClassTask.objects.all().filter(status='Overdue').order_by('task_priority')
    if tasks:
        #debug_task.delay()
        # data = TaskSerializer(tasks)
        return Response(TaskSerializernormal(tasks, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
