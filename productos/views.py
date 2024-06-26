from django.shortcuts import redirect, render
from .models import Producto, Categoria
from django.contrib import messages


# PRODUCTOS

def productos(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()

    return render(request,
                  "productos.html",
                  context={"productos": productos,
                           "categorias": categorias
                           })

def agregar_producto(request):
    nombre = request.POST["txtNombre"]
    precio = request.POST["txtPrecio"]
    stock = request.POST["txtStock"]
    categoria = request.POST["categoria"]

    try:
        producto = Producto.objects.create(
            nombre=nombre, precio=precio, stock=stock,
            categoria=Categoria.objects.get(id=categoria)
        )
    except Exception as e:
        messages.error(request, e)
    else:
        messages.success(request, "Producto agregado correctamente! ")
    
    return redirect("/productos")

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    messages.success(request, "Producto eliminado correctamente! ")

    return redirect("/productos")

def editar_producto(request, id):
    if request.method == "POST":
        nombre = request.POST["txtNombre"]
        precio = request.POST["txtPrecio"]
        stock = request.POST["txtStock"]
        categoria = request.POST["categoria"]

        try:
            producto = Producto.objects.get(id=id)
            producto.nombre = nombre
            producto.precio = precio
            producto.stock = stock
            producto.categoria = Categoria.objects.get(id=categoria)

            producto.save()

        except Exception as e:
            messages.error(request, e, "No se ha podido actualizar el producto")
        
        else:
            messages.success(request, "El producto se ha actualizado correctamente! ")

        finally:
            return redirect("/productos")

    producto = Producto.objects.get(id=id)
    categorias = Categoria.objects.all()

    return render(request,
                  "editar_producto.html",
                  context={"producto": producto,
                           "categorias": categorias
                           })


# CATEGORIAS

def agregar_categoria(request):
    nombre = request.POST["Categoria"]

    try:
        categoria = Categoria.objects.create(
            nombre=nombre,
        )
    except Exception as e:
        messages.error(request, e)
    else:
        messages.success(request, "Categoria agregada correctamente! ")
    
    return redirect("/productos")

def eliminar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    messages.success(request, "Categoria eliminada correctamente! ")

    return redirect("/productos")

def editar_categoria(request, id):
    if request.method == "POST":
        nombre = request.POST["Categoria"]

        try:
            categoria = Categoria.objects.get(id=id)
            categoria.nombre = nombre
            
            categoria.save()

        except Exception as e:
            messages.error(request, e, "No se ha podido actualizar la categoria")
        
        else:
            messages.success(request, "La categoria se ha actualizado correctamente! ")

        finally:
            return redirect("/productos")

    categoria = Categoria.objects.get(id=id)

    return render(request,
                  "editar_categoria.html",
                  context={"categoria": categoria,
                           })

