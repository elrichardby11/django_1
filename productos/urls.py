from django.urls import path
from . import views


urlpatterns = [
    path('', views.productos, name="productos"),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('eliminar_producto/<id>', views.eliminar_producto, name="eliminar_producto"),
    path('editar_producto/<id>', views.editar_producto, name="editar_producto"),
]