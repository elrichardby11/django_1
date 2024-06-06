from django.urls import path
from . import views 

urlpatterns = [
    path('', views.listaEmpleados),
    path('registrar_empleado/', views.registrarEmpleado),
]