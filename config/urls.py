from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tareas.urls')),
    path('', include('django_prometheus.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('tareas.urls')),
]