from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Task
from .permissions import IsOwnerOrReadOnly
from .serializers import UpdateTaskSerializer, UserSerializer, TaskSerializerAll, TaskSerializer


# Creating API views for User to retrieve username
class UserList(ListAPIView, RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# # Creating API view for GET request to retrieve list of all tasks
# class ShowAllTasks(ListAPIView):
#     queryset = Task.objects.all().order_by("-status", 'deadline', 'priority')
#     serializer_class = TaskSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#
# # Creating Api view for POST request to create a new task
# class CreateTask(CreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = UpdateTaskSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
#
#
# # Creating API view for PUT,PATCH request to update a single task
# class UpdateTask(UpdateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = UpdateTaskSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly]
#
#
# # Creating API view for DELETE, GET request to delete or show a single task
# class ShowDeleteTask(RetrieveDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializerAll
#
#
# # Creating API view for GET request to retrieve overdue tasks
# class ShowOverdue(ListAPIView):
#     queryset = Task.objects.all().filter(status='Overdue').order_by('priority', 'deadline')
#     serializer_class = TaskSerializerAll
class SingleTask(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all().order_by("-status", 'deadline', 'priority')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TaskSerializerAll
        else:
            return UpdateTaskSerializer

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CreateViewTasks(CreateAPIView, ListAPIView):
    queryset = Task.objects.all().order_by("-status", 'deadline', 'priority')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TaskSerializer
        else:
            return UpdateTaskSerializer

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
