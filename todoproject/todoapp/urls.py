from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.TaskOverview, name='home'),
#     path('create/', views.add_tasks, name='add-tasks'),
#     path('all/', views.view_tasks, name="view-tasks"),
#     path('update/<int:pk>/', views.update_task, name='update-tasks'),
#     path('task/delete/<int:pk>', views.delete_tasks, name='delete-tasks'),
#     path('task/<int:pk>/', views.view_task, name='view-task'),
#     path('task/overdue/',views.overdue_tasks, name='overdue-tasks')
# ]
from .views import *

urlpatterns = [
    path('Task/Show/',ShowAllTasks.as_view(),name='Hello'),
    #path('Show a task/<int:pk>',ShowSingleTask.as_view()),
    #path('Delete a task/<int:pk>',DeleteTask.as_view()),
    path('Task/Create/',CreateTask.as_view()),
    path('Task/Udpate/<int:pk>',UpdateTask.as_view()),
    path('Task/Overdue/',ShowOverdue.as_view()),

path('users/', views.UserList.as_view()),
path('users/<int:pk>/', views.UserDetail.as_view()),
    ]

# urlpatterns = [
#
# path('Show all tasks/',ShowAllTasks.as_view()),
#     path('Create a task/',CreateTask.as_view()),
#     path('Update a task/<int:pk>',UpdateTask.as_view()),
#
#     ]
