from django.db import models

class ClasesGrupales(models.Model):
    id_clase = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo_entrenamiento = models.CharField(max_length=50)
    profesor = models.CharField(max_length=100)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    lugar = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.fecha}"