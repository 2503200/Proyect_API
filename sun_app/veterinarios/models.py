from django.db import models

class Consultorio(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    horas = models.IntegerField(null=True)
    propietario = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.nombre}'

class Especialidad(models.Model):
    nombre = models.CharField(max_length=30, null=True)
    horas = models.IntegerField(null=True)
    herramientas = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.nombre}'

    # Create your models here.
class Veterinario(models.Model):
    SEXO = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True)
    email = models.CharField(max_length=50)
    numero_celular = models.CharField(max_length=10)
    activo = models.BooleanField(default=True)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.SET_NULL, null=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'id: {self.id} - {self.nombre} {self.apellido}'

