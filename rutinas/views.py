from django.shortcuts import render
def mis_rutinas(request):
    return render(request, 'rutinas/mis_rutinas.html')

def crear_rutina(request):
    return render(request, 'rutinas/crear_rutina.html')