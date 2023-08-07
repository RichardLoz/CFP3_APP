from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('administracion.urls')),
    path('admin/', admin.site.urls),
    path('profesores/', include('profesor.urls')),
    path('cursos/', include('administracion.urls')),
]
