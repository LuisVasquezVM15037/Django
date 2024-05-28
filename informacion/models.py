from django.db import models

# Create your models here.

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    descripcion = models.TextField(verbose_name='descripcion', null=True)


def __str__(self):
    fila = "nombre: " + self.nombre + " - " +"email: " + self.email+ " - " +" descripcion: " + self.descripcion
    return self.fila


