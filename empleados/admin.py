from django.contrib import admin
from .models import Empleado

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ["rut", "nombre", "apellido", "correo", "fechaNacimiento", "pais", "genero", "creadoEn", "actualizadoEn"]
    # exclude = ("apellido", ) # Lo excluye en la lista añadir
    # fields = ("rut", "nombre", ) # Solo muestra los campos en la lista añadir

admin.site.register(Empleado, EmpleadoAdmin)