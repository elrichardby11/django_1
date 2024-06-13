from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from empleados.models import Empleado
from django.contrib.auth.decorators import login_required

def listaEmpleados(request):
    empleados = Empleado.objects.all()
    return render(request, "lista_empleados.html",context={"empleados": empleados,})

@login_required
def registrarEmpleado(request):
    rut = request.POST['txtRut']
    nombre = request.POST["txtNombre"]
    apellido = request.POST["txtApellido"]
    correo = request.POST["txtCorreo"]
    fecha = request.POST["Fecha"]
    pais = request.POST["Pais"]
    genero = request.POST["Genero"]

    try:
        # Crear empleado 
        empleado = Empleado.objects.create(
            rut=rut, nombre=nombre, apellido=apellido,
            correo=correo, fechaNacimiento=fecha, pais=pais, genero=genero
        )
    except Exception as e:
        if e.__class__.__name__ == "IntegrityError":
            if "rut" in e.args[0]:
                e = "El rut ingresado ya existe! "
            elif "correo" in e.args[0]:
                e = "El correo ingresado ya existe! "
        messages.error(request, f"Error al crear empleado: {e}")
    else:
        messages.success(request, "Empleado registrado correctamente! ")
    finally:
        return redirect("/empleados")
    
@login_required
def editarEmpleado(request, rut):
    empleado = Empleado.objects.get(rut=rut)
    return render(request, "editar_empleado.html",context={"empleado": empleado,})

@login_required
def actualizarEmpleado(request):
    try:
        rut = request.POST['txtRut']
        nombre = request.POST["txtNombre"]
        apellido = request.POST["txtApellido"]
        correo = request.POST["txtCorreo"]
        fecha = request.POST["Fecha"]
        pais = request.POST["Pais"]
        genero = request.POST["Genero"]

        empleado = Empleado.objects.get(rut=rut)
        empleado.rut= rut
        empleado.nombre = nombre
        empleado.apellido = apellido
        empleado.correo = correo
        empleado.fechaNacimiento = fecha
        empleado.pais = pais
        empleado.genero = genero

        empleado.save()
    except Exception as e:
        messages.error(request, f"Error al crear empleado: {e}")
    else:
        messages.success(request, "Empleado editado correctamente! ")
    finally:
        return redirect('/empleados')

@login_required
def eliminarEmpleado(request, rut):
    try:
        empleado = Empleado.objects.get(rut=rut)
        empleado.delete()
    except Exception as e:
        messages.error(request, f"Error al crear empleado: {e}")
    else:
        messages.success(request, "Empleado eliminado correctamente! ")
    finally:
        return redirect('/empleados')