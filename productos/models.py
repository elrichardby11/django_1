from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.nombre}"

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField(default=0)
    precio = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creado_en = models.DateField(auto_now_add=True)