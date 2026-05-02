from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Plan,Membresia
from usuarios.models import Usuario
from django.shortcuts import get_object_or_404
from rutinas.models import Rutina

def intro(request):
    return render(request, 'gimnasio/intro.html')

def sobreNosotros(request):
    return render(request, 'gimnasio/sobreNosotros.html')

def planes(request):
    mostrar_todos_planes= Plan.objects.all()
    return render(request, 'gimnasio/planes.html',{'planes':mostrar_todos_planes})

#home
@login_required
def inicio(request):
    print("Usuario actual:", request.user)
    print("ID usuario:", request.user.id)

    membresia_activa = Membresia.objects.filter(
        id_usuario=request.user,
        estado='activa'
    ).first()

    if not membresia_activa:
        return redirect('planes')

    # Rutina del día (admin)
    predeterminada = Rutina.objects.filter(
        tipo_rutina='predeterminada'
    ).order_by('-fecha_creacion').first()

    # Rutinas del usuario
    rutinasUsuario = Rutina.objects.filter(
        id_usuario=request.user,
        tipo_rutina='personal'
    )

    return render(request, 'gimnasio/inicio.html', {'rutina': predeterminada,'rutinas': rutinasUsuario})


#COMPRAR EL PLAN
def comprar_plan(request, id_plan):
    plan = get_object_or_404(Plan, id_plan=id_plan)
    membresia_activa=Membresia.objects.filter(
        id_usuario=request.user,
        estado='activa'
    ).first()
    if membresia_activa:
        return render(request, 'gimnasio/membresia_activa.html', {
            'membresia': membresia_activa
        })
    return render(request, 'gimnasio/comprar_plan.html', {'plan': plan})

def galeria(request):
    return render(request, 'gimnasio/galeria.html')

#PANEL DEL ADMINISTRADOR
def panel_admin(request):
    if not request.user.es_admin():
        return redirect('inicio')
    
    total_usuarios = Usuario.objects.filter(rol='cliente').count()
    total_planes = Plan.objects.all().count()
    membresias_activas = Membresia.objects.filter(estado='activa').count()

    return render(request, 'gimnasio/panel_admin.html',{
        'total_usuarios': total_usuarios,
        'total_planes': total_planes,
        'membresias_activas': membresias_activas,
    })
#PANEL DE ADMI (GESTIONAR LA INFORMACION DE LOS USUARIOS)

def admin_usuarios(request):
    if not request.user.es_admin():
        return redirect('inicio')

    usuarios = Usuario.objects.filter(rol='cliente')
    
    return render(request, 'gimnasio/administrar_usuarios.html', {
        'usuarios': usuarios
    })

#PERMITE CAMBIAR EL ESTADO DE LOS USUARIOS

@login_required

def admin_cambiar_estado_usuario(request, id_usuario):
        if not request.user.es_admin():
            return redirect('inicio')
        usuario=get_object_or_404(Usuario, id=id_usuario)
        
        if usuario.estado == 'activo':
            usuario.estado = 'suspendido'
        else:
            usuario.estado = 'activo'
        
        usuario.save()
        return redirect('admin_usuarios')
#PERMITE EDITAR, CREAR, ELIMINAR LOS PLANES
@login_required
def administrar_planes(request):
    if not request.user.es_admin():
            return redirect('inicio')
    planes=Plan.objects.all()
    return render(request,'administrar_planes.html',{
         'planes':planes
    })
@login_required
def crear_planes(request):
    if not request.user.es_admin():
            return redirect('inicio')
    if request.method == 'POST':
        nombre=request.POST['nombre_plan']
        precio=request.POST['precio']
        duracion=request.POST['duracion_dias']
        descripcion=request.POST['descripcion']

        Plan.objects.create(
            nombre_plan=nombre,
            precio=precio,
            duracion_dias=duracion,
            descripcion=descripcion
        )
        return redirect('admin_planes')
    
    return render(request, 'gimnasio/admin_crear_plan.html')
@login_required
def eliminarPlan(request, id_plan):
    if not request.user.es_admin():
        return redirect('inicio')
    plan = get_object_or_404(Plan,id_plan=id_plan )
    plan.delete()
    return redirect('admin_planes')

