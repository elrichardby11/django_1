from django.urls import path
from . import views 

urlpatterns = [
    path('', views.listaEmpleados),
    path('registrar_empleado/', views.registrarEmpleado),
    path('editar_empleado/<rut>', views.editarEmpleado),
    path('editar_empleado/actualizar_empleado/', views.actualizarEmpleado),
    path('eliminar_empleado/<rut>', views.eliminarEmpleado),
]