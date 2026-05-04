from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_rutinas, name='lista_rutinas'),
    path('crear/', views.crear_rutina, name='crear_rutina'),
    path('<int:pk>/editar/', views.editar_rutina, name='editar_rutina'),
    path('<int:pk>/eliminar/', views.eliminar_rutina, name='eliminar_rutina'),
    path('<int:pk>/', views.detalle_rutina, name='detalle_rutina'),
    path('<int:pk>/iniciar/', views.iniciar_entrenamiento, name='iniciar_entrenamiento'),
    path('sesion/<int:pk>/', views.ejecutar_rutina, name='ejecutar_rutina'),
    path('sesion/guardar-serie/', views.guardar_serie, name='guardar_serie'),
    path('sesion/<int:pk>/finalizar/', views.finalizar_sesion, name='finalizar_sesion'),
    path('historial/', views.historial, name='historial'),
]