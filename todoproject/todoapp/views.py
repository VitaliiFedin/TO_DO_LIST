from django.shortcuts import render
import os
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Task as ClassTask
from .serializers import TaskSerializerAll
from .serializers import TaskSerializer, SingleTaskSerializer,UserSerializer
from rest_framework import serializers, viewsets
from rest_framework import status
from celery import *
from django.utils import timezone
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from todoapp.permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User


# class ShowSingleTask(generics.RetrieveAPIView):
#     queryset = ClassTask.objects.all()
#     serializer_class = SingleTaskSerializer
#
#
# class DeleteTask(generics.DestroyAPIView):
#     queryset = ClassTask.objects.all()

class ShowAllTasks(generics.ListAPIView):
    queryset = ClassTask.objects.all().order_by("-status", 'deadline', 'task_priority')
    serializer_class = TaskSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CreateTask(generics.CreateAPIView):
    queryset = ClassTask.objects.all()
    serializer_class = TaskSerializerAll


class UpdateTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassTask.objects.all()
    serializer_class = TaskSerializerAll


class ShowOverdue(generics.ListAPIView):
    queryset = ClassTask.objects.all().filter(status='Overdue').order_by('task_priority', 'deadline')
    serializer_class = SingleTaskSerializer



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# @api_view(['GET'])
# def TaskOverview(request):
#     api_urls = {
#         'All tasks': '/all',
#         'All tasks specific fileds':'/specific',
#         'Single task': '/task/pk',
#         'Create': '/create',
#         'Update': '/update/pk',
#         'Delete': '/task/delete/pk',
#         'Overdue': 'task/overdue/'
#     }
#
#     return Response(api_urls)
#
#
# @api_view(['POST'])
# def add_tasks(request):
#     task = TaskSerializerAll(data=request.data)
#     if ClassTask.objects.filter(**request.data).exists():
#         raise serializers.ValidationError('This data already exists')
#
#     if task.is_valid():
#         task.save()
#         # debug_task.delay()
#         return Response(task.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['GET'])
# def view_tasks(request):
#     if request.query_params:
#         tasks = ClassTask.objects.filter(**request.query_param.dict())
#     else:
#         tasks = ClassTask.objects.all().order_by("-status", 'task_priority')
#     if tasks:
#
#         return Response(SingleTaskSerializer(tasks, many=True).data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['PUT'])
# def update_task(request, pk):
#     task = ClassTask.objects.get(pk=pk)
#     data = TaskSerializerAll(task, data=request.data, partial=True)
#     data_view = SingleTaskSerializer(task, many=False)
#
#     if data.is_valid():
#         data.save()
#         return Response(data_view.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['DELETE'])
# def delete_tasks(request, pk):
#     task = get_object_or_404(ClassTask, pk=pk)
#     task.delete()
#     return Response(status=status.HTTP_202_ACCEPTED)
#
#
# @api_view(['GET'])
# def view_task(request, pk):
#     tasks = ClassTask.objects.get(pk=pk)
#     serializer = SingleTaskSerializer(tasks, many=False)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def overdue_tasks(request):
#     if request.query_params:
#         tasks = ClassTask.objects.filter(**request.query_param.dict())
#     else:
#         tasks = ClassTask.objects.all().filter(status='Overdue').order_by('task_priority','deadline')
#     if tasks:
#         return Response(SingleTaskSerializer(tasks, many=True).data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
