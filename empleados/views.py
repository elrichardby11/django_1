from django.shortcuts import redirect, render
from empleados.models import Empleado

def listaEmpleados(request):
    empleados = Empleado.objects.all()
    return render(request, "lista_empleados.html",context={"empleados": empleados,})

def registrarEmpleado(request):
    rut = request.POST['txtRut']
    nombre = request.POST["txtNombre"]
    apellido = request.POST["txtApellido"]
    correo = request.POST["txtCorreo"]
    fecha = request.POST["Fecha"]
    pais = request.POST["Pais"]
    genero = request.POST["Genero"]

    # Crear empleado 
    empleado = Empleado.objects.create(
        rut=rut, nombre=nombre, apellido=apellido,
        correo=correo, fechaNacimiento=fecha, pais=pais, genero=genero
    )
    return redirect("/empleados")
    