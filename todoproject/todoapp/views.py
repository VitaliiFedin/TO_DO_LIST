from .models import Task as ClassTask
from .permissions import IsOwnerOrReadOnly
from .serializers import TaskSerializer, UpdateTaskSerializer, UserSerializer, TaskSerializerAll
from rest_framework import generics
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


# Creating API views for User to retrieve username
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Creating API view for GET request to retrieve list of all tasks
class ShowAllTasks(generics.ListAPIView):
    queryset = ClassTask.objects.all().order_by("-status", 'deadline', 'task_priority')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Creating Api view for POST request to create a new task
class CreateTask(generics.CreateAPIView):
    queryset = ClassTask.objects.all()
    serializer_class = UpdateTaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Creating API view for PUT,PATCH request to update a single task
class UpdateTask(generics.UpdateAPIView):
    queryset = ClassTask.objects.all()
    serializer_class = UpdateTaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


# Creating API view for DELETE, GET request to delete or show a single task
class ShowDeleteTask(generics.RetrieveDestroyAPIView):
    queryset = ClassTask.objects.all()
    serializer_class = TaskSerializerAll


# Creating API view for GET request to retrieve overdue tasks
class ShowOverdue(generics.ListAPIView):
    queryset = ClassTask.objects.all().filter(status='Overdue').order_by('task_priority', 'deadline')
    serializer_class = TaskSerializerAll
