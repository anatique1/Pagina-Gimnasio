from django.contrib import admin
from .models import Rutina, Ejercicio, RutinaEjercicio

admin.site.register(Rutina)
admin.site.register(Ejercicio)
admin.site.register(RutinaEjercicio)