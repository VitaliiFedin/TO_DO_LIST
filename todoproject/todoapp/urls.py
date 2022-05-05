from django.urls import path

from .views import *

urlpatterns = [path('task/<int:pk>', SingleTask.as_view()),
path('tasks/', CreateViewTasks.as_view()),
               ]
