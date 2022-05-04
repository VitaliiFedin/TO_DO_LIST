from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from .yasg import urlpatterns as yasg_patterns
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todoapp.urls')),
    path('', RedirectView.as_view(url='swagger/')),
]
urlpatterns += yasg_patterns
