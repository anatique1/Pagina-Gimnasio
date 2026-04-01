from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROLES = [
        ('cliente', 'Cliente'),
        ('admin', 'Administrador'),
    ]
   
    rol = models.CharField(max_length=20, choices=ROLES, default='cliente')
    telefono = models.CharField(null=True, blank=True)
    tipo_documento = models.CharField(max_length=20, null=True, blank=True)
    documento = models.CharField(max_length=20, null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def es_admin(self):
        return self.rol == 'admin'

    def __str__(self):
        return self.email