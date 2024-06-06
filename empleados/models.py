from django.db import models

_GENERO = {
    "F": "Femenino",
    "M": "Masculino",
    "O": "Otro",
}

_PAISES = {
    "CL": "Chile",
    "AR": "Argentina",
    "BR": "Brasil",
}



class Empleado(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255, blank=True)
    correo = models.CharField(max_length=255, unique=True)
    fechaNacimiento = models.DateField(default="01/01/2000", verbose_name="Fecha de Nacimiento")
    pais = models.CharField(max_length=20, choices=_PAISES, default=_PAISES["CL"])
    genero = models.CharField(max_length=1, choices=_GENERO)
    creadoEn = models.DateTimeField(auto_now_add=True)
    actualizadoEn = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"