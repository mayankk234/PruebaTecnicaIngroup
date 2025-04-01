from django.urls import path
from .views import post_user, get_users  # Asegúrate de importar las vistas

urlpatterns = [
    path('users/', get_users, name='get_users'),  # Ruta para obtener los usuarios
    path('users/create/', post_user, name='post_user'),  # Ruta para crear un nuevo usuario
]
