from django.db import models
from usuarios.models import Usuario

class Ejercicio(models.Model):
    GRUPOS = [
        ('pecho', 'Pecho'),
        ('espalda', 'Espalda'),
        ('hombros', 'Hombros'),
        ('biceps', 'Bíceps'),
        ('triceps', 'Tríceps'),
        ('piernas', 'Piernas'),
        ('gluteos', 'Glúteos'),
        ('core', 'Core'),
        ('cardio', 'Cardio'),
    ]
    id_ejercicio = models.AutoField(primary_key=True)
    nombreEjercicio = models.CharField(max_length=100)
    descripcion = models.TextField()
    grupo_muscular = models.CharField(max_length=20, choices=GRUPOS, default='core')
    imagen = models.ImageField(upload_to='ejercicios/', blank=True, null=True)
    video = models.FileField(upload_to='ejercicios/videos/', blank=True, null=True)
    
    def __str__(self):
        return self.nombreEjercicio


class Rutina(models.Model):
    TIPO_RUTINA = [
        ('predeterminada', 'Predeterminada'),
        ('personal', 'Personal'),
    ]
    TIPO_ENTRENAMIENTO = [
        ('crossfit',     'CrossFit'),
        ('fuerza',       'Fuerza'),
        ('cardio',       'Cardio'),
        ('funcional',    'Funcional'),
        ('hipertrofia',  'Hipertrofia'),
        ('flexibilidad', 'Flexibilidad'),
    ]
    NIVELES = [
        ('principiante', 'Principiante'),
        ('intermedio',   'Intermedio'),
        ('avanzado',     'Avanzado'),
    ]
    DIAS = [
        ('lun', 'Lunes'),
        ('mar', 'Martes'),
        ('mie', 'Miércoles'),
        ('jue', 'Jueves'),
        ('vie', 'Viernes'),
        ('sab', 'Sábado'),
        ('dom', 'Domingo'),
    ]

    id_rutina = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='rutinas')
    nombre_rutina = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500, blank=True)
    tipo_rutina = models.CharField(max_length=20, choices=TIPO_RUTINA, default='personal')
    tipo_entrenamiento = models.CharField(max_length=20, choices=TIPO_ENTRENAMIENTO, default='funcional')
    duracion = models.IntegerField(default=45)
    nivel = models.CharField(max_length=20, choices=NIVELES, default='principiante')
    dias = models.CharField(max_length=50, blank=True)
    creada_en = models.DateTimeField(auto_now_add=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_rutina

    def get_dias_lista(self):
        return self.dias.split(',') if self.dias else []

    def get_dias_display(self):
        dias_dict = dict(self.DIAS)
        return ', '.join([dias_dict.get(d, d) for d in self.get_dias_lista()])


class RutinaEjercicio(models.Model):
    id_rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name='ejercicios')
    id_ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, related_name='rutinas')
    series = models.IntegerField(default=3)
    repeticiones = models.IntegerField(default=12)
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"{self.id_rutina} - {self.id_ejercicio}"

class RutinaEjercicio(models.Model):
    id_rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name='ejercicios')
    id_ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, related_name='rutinas')
    series = models.IntegerField(default=3)
    repeticiones = models.IntegerField(default=12)
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"{self.id_rutina} - {self.id_ejercicio}"


class SesionEntrenamiento(models.Model):
    rutina   = models.ForeignKey(Rutina,   on_delete=models.CASCADE, related_name='sesiones')
    usuario  = models.ForeignKey(Usuario,  on_delete=models.CASCADE, related_name='sesiones')
    fecha_inicio  = models.DateTimeField(auto_now_add=True)
    fecha_fin     = models.DateTimeField(null=True, blank=True)
    duracion_real = models.IntegerField(null=True, blank=True)
    completada    = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f"{self.usuario} - {self.rutina} - {self.fecha_inicio.strftime('%d/%m/%Y %H:%M')}"

    def calcular_duracion(self):
        if self.fecha_inicio and self.fecha_fin:
            diff = self.fecha_fin - self.fecha_inicio
            self.duracion_real = int(diff.total_seconds() / 60)
            self.save()


class SerieSesion(models.Model):
    sesion           = models.ForeignKey(SesionEntrenamiento, on_delete=models.CASCADE, related_name='series')
    rutina_ejercicio = models.ForeignKey(RutinaEjercicio,     on_delete=models.CASCADE, related_name='series_sesion')
    numero_serie            = models.IntegerField(default=1)
    peso_kg                 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    repeticiones_realizadas = models.IntegerField(default=0)
    tiempo_descanso         = models.IntegerField(default=0)  # en segundos
    completada              = models.BooleanField(default=False)

    class Meta:
        ordering = ['numero_serie']

    def __str__(self):
        return f"Serie {self.numero_serie} - {self.rutina_ejercicio.id_ejercicio.nombreEjercicio}"