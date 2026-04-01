from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        if request.user.es_admin():
            return redirect('panel_admin')
        else:
            return redirect('inicio')
    return render(request, 'usuarios/login.html')

@login_required
def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('inicio')

def redirigir_por_rol(request):
    if request.user.is_authenticated:
        print("USUARIO:", request.user.email)
        print("ROL:", request.user.rol)
        if request.user.es_admin():
            return redirect('panel_admin')
        else:
            return redirect('inicio')
    return redirect('login')