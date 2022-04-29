from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskOverview, name='home'),
    path('create/', views.add_tasks, name='add-tasks'),
    path('all/', views.view_tasks, name="view-tasks"),
    path('update/<int:pk>/',views.update_task, name='update-tasks'),
    path('task/<int:pk>/delete',views.delete_tasks, name='delete-tasks'),
]
