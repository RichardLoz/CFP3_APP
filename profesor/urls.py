from django.urls import path
from .views import *

urlpatterns = [
    path('', list_profesores),
    path('guardar/', store_profesor, name='store_profesor'),
    path('actualizar/<id>', update_profesor, name='update_profesor'),
    path('eliminar/<id>', delete_profesor, name='delete_profesor'),
]
