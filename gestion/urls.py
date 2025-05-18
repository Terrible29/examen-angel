from django.urls import path
from . import views  # o from .views import crear_autor, etc.

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear-autor/', views.crear_autor, name='crear_autor'),
    path('listar-autores/', views.listar_autores, name='listar_autores'),
    path('editar-autor/<int:id>/', views.editar_autor, name='editar_autor'),
    path('eliminar-autor/<int:id>/', views.eliminar_autor, name='eliminar_autor'),

    path('crear-libro/', views.crear_libro, name='crear_libro'),
    path('listar-libros/', views.listar_libros, name='listar_libros'),
    path('editar-libro/<int:id>/', views.editar_libro, name='editar_libro'),
    path('eliminar-libro/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
]
