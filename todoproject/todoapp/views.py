from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Task
from .permissions import IsOwnerOrReadOnly
from .serializers import UpdateTaskSerializer, UserSerializer, TaskSerializerAll, TaskSerializer


class UserList(ListAPIView, RetrieveAPIView):
    """
    This class retrieves user information

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SingleTask(RetrieveUpdateDestroyAPIView):
    """
    This class uses queryset and serializer to send GET, PUT, DELETE, PATCH requests.

    Returns :
        GET,POST requests.

    """
    queryset = Task.objects.all().order_by("-status", 'deadline', 'priority')

    def get_serializer_class(self):
        """

        This function allows to chose specific serializer for each method

        Returns:
            Serializer.
        """
        if self.request.method == 'GET':
            return TaskSerializerAll
        else:
            return UpdateTaskSerializer

    # Adding permissions for viewing, editing, deleting task
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CreateViewTasks(CreateAPIView, ListAPIView):
    """
    This class uses queryset and serializer to send GET, POST requests.

    Returns:
        GET POST request.

    """
    queryset = Task.objects.all().order_by("-status", 'deadline', 'priority')

    def get_serializer_class(self):
        """
        This function allows to choose specific serializer for each method.

        Returns:
            Serializer.
        """
        if self.request.method == 'GET':
            return TaskSerializer
        else:
            return UpdateTaskSerializer

    # Adding permissions for viewing, creating tasks
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
