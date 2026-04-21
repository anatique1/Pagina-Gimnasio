from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_rutinas, name='lista_rutinas'),
    path('crear/', views.crear_rutina, name='crear_rutina'),
    path('<int:pk>/editar/', views.editar_rutina, name='editar_rutina'),
    path('<int:pk>/eliminar/', views.eliminar_rutina, name='eliminar_rutina'),
    path('<int:pk>/', views.detalle_rutina, name='detalle_rutina'),
]