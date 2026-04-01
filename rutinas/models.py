from django.db import models
from usuarios.models import Usuario

class Ejercicio(models.Model):
    id_ejercicio= models.AutoField(primary_key=True)   
    nombreEjercicio=models.CharField(max_length=100)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre
class Rutina(models.Model):
    TIPO_RUTINA = [
        ('predeterminada','Predeterminada'),
        ('personal','Personal'),
        ]
    id_rutina = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='rutinas')
    nombre_rutina = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo_rutina = models.CharField(max_length=20, choices=TIPO_RUTINA, default='personal')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_rutina


class RutinaEjercicio(models.Model):
    id_rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name='ejercicios')
    id_ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, related_name='rutinas')
    series = models.IntegerField()
    repeticiones = models.IntegerField()

    def __str__(self):
        return f"{self.id_rutina} - {self.id_ejercicio}"

