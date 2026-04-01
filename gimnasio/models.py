from django.db import models
from usuarios.models import Usuario

class Plan(models.Model):
    id_plan = models.AutoField(primary_key=True)    
    nombre_plan = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_dias = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_plan


class Membresia(models.Model):
    ESTADOS = [
        ('activa', 'Activa'),
        ('vencida', 'Vencida'),
        ('cancelada', 'Cancelada'),
    ]
    MEDIOS_PAGO = [
        ('wompi', 'Wompi'),
        ('efectivo', 'Efectivo'),
        ('nequi', 'Nequi'),
    ]
    id_membresia = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='membresias')
    id_plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='membresias')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='activa')
    fecha_pago = models.DateField()
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    medio_pago = models.CharField(max_length=20, choices=MEDIOS_PAGO)

    def verificar_vigencia(self):
        from datetime import date
        return self.fecha_fin >= date.today() and self.estado == 'activa'

    def __str__(self):
        return f"{self.id_usuario} - {self.id_plan}"


class PagoEnLinea(models.Model):
    ESTADOS_PAGO = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    ]
    id_pago = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pagos')
    id_plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='pagos')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(auto_now_add=True)
    documento = models.CharField(max_length=20)
    estado_pago = models.CharField(max_length=20, choices=ESTADOS_PAGO, default='pendiente')

    def __str__(self):
        return f"Pago {self.id_pago} - {self.id_usuario}"