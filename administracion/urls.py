from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index_view, name='index'),
    path('cursos/', list_cursos),
    path('guardar/', store_curso, name='store_curso'),
    path('actualizar/<id>', update_curso, name='update_curso'),
    path('eliminar/<id>', delete_curso, name='delete_curso'),

]