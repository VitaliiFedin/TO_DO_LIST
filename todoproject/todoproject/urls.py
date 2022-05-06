from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from .yasg import urlpatterns as yasg_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todoapp.urls')),
    path('', RedirectView.as_view(url='swagger/')),
]
# Adding yasg urlpatterns to exists
urlpatterns += yasg_patterns
