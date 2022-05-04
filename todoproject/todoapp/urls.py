from django.urls import path, include
from django.views.generic import RedirectView

from . import views
from .views import *

urlpatterns = [
    path('Tasks/Show/', ShowAllTasks.as_view(), name='show_all'),
    path('Task/Create/', CreateTask.as_view(), name='create_task'),
    path('Task/<int:pk>', ShowDeleteTask.as_view(), name='show_delete'),
    path('Task/Overdue/', ShowOverdue.as_view(), name='overdue_task'),
    path('Task/Update/<int:pk>', UpdateTask.as_view(), name='update_task'),
    path('auth/', include('rest_framework.urls')),
    path('auth', RedirectView.as_view(url='auth/login/'), name='login'),
]
