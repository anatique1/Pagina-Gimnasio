from django.urls import path
from . import views

urlpatterns = [
    path('', views.mis_rutinas, name='mis_rutinas'),
    path('crear/', views.crear_rutina, name='crear_rutina'),
]