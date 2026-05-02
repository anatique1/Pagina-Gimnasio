from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ejercicio, RutinaEjercicio, Rutina


@login_required
def lista_rutinas(request):
    rutinas = Rutina.objects.filter(id_usuario=request.user).order_by('-creada_en')
    return render(request, 'rutinas/lista.html', {
        'rutinas': rutinas
    })


@login_required
def crear_rutina(request):
    ejercicios_disponibles = Ejercicio.objects.all().order_by('grupo_muscular', 'nombreEjercicio')

    if request.method == 'POST':
        rutina = Rutina.objects.create(
            id_usuario=request.user,
            nombre_rutina=request.POST['nombre_rutina'],
            descripcion=request.POST.get('descripcion', ''),
            nivel=request.POST['nivel'],
            dias=','.join(request.POST.getlist('dias')),
        )

        for ejercicio in ejercicios_disponibles:
            if request.POST.get(f'ejercicio_{ejercicio.pk}'):
                RutinaEjercicio.objects.create(
                    id_rutina=rutina,
                    id_ejercicio=ejercicio,
                    series=request.POST.get(f'series_{ejercicio.pk}', 3),
                    repeticiones=request.POST.get(f'reps_{ejercicio.pk}', 12),
                    orden=ejercicio.pk
                )
        return redirect('lista_rutinas')

    return render(request, 'rutinas/crear_rutinas.html', {
        'ejercicios': ejercicios_disponibles,
        'dias_choices': Rutina.DIAS,
        'dias_seleccionados': [],
        'ejercicios_seleccionados': [],
    })


@login_required
def editar_rutina(request, pk):
    rutina = get_object_or_404(Rutina, pk=pk, id_usuario=request.user)
    ejercicios_disponibles = Ejercicio.objects.all().order_by('grupo_muscular', 'nombreEjercicio')

    if request.method == 'POST':
        rutina.nombre_rutina = request.POST['nombre_rutina']
        rutina.descripcion   = request.POST.get('descripcion', '')
        rutina.nivel         = request.POST['nivel']
        rutina.dias          = ','.join(request.POST.getlist('dias'))
        rutina.save()

        rutina.ejercicios.all().delete()
        for ejercicio in ejercicios_disponibles:
            if request.POST.get(f'ejercicio_{ejercicio.pk}'):
                RutinaEjercicio.objects.create(
                    id_rutina=rutina,
                    id_ejercicio=ejercicio,
                    series=request.POST.get(f'series_{ejercicio.pk}', 3),
                    repeticiones=request.POST.get(f'reps_{ejercicio.pk}', 12),
                    orden=ejercicio.pk
                )
        return redirect('lista_rutinas')

    ejercicios_actuales = rutina.ejercicios.all()
    datos_ejercicios = {}
    for re in ejercicios_actuales:
        datos_ejercicios[re.id_ejercicio.pk] = {
            'series': re.series,
            'reps': re.repeticiones,
        }

    return render(request, 'rutinas/crear_rutinas.html', {
        'rutina': rutina,
        'ejercicios': ejercicios_disponibles,
        'dias_choices': Rutina.DIAS,
        'dias_seleccionados': rutina.get_dias_lista(),
        'datos_ejercicios': datos_ejercicios,
        'ejercicios_seleccionados': list(datos_ejercicios.keys()),
    })


@login_required
def eliminar_rutina(request, pk):
    rutina = get_object_or_404(Rutina, pk=pk, id_usuario=request.user)
    if request.method == 'POST':
        rutina.delete()
    return redirect('lista_rutinas')


@login_required
def detalle_rutina(request, pk):
    rutina = get_object_or_404(Rutina, pk=pk, id_usuario=request.user)
    return render(request, 'rutinas/detalle.html', {
        'rutina': rutina
    })