from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('planes/', views.planes, name='planes'),
    path('sobreNosotros/', views.sobreNosotros, name='sobreNosotros'),
    path('galeria/', views.galeria, name='galeria'),
    path('comprar/<int:id_plan>/',views.comprar_plan, name = 'comprar_plan'),
    path('panel_admin/', views.panel_admin, name='panel_admin'),
    path('panel_admin_usuarios/',views.admin_usuarios,name= 'panel_admin_usuarios'),
    path('panel_admin/usuarios/<int:id_usuario>/estado/',views.admin_cambiar_estado_usuario, name='admin_cambiar_estado_usuario'),
    path('panel_admin/planes/', views.administrar_planes, name='administrar_planes'),
    path('panel_admin/planes/crear/', views.crear_planes, name='crear_planes'), 
    path('panel_admin/planes/<int:id_plan>/eliminar/', views.eliminarPlan, name='eliminarPlan'),

]