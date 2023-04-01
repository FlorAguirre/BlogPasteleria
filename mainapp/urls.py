from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.login_page, name = 'login'),
    path('inicio/', views.index, name = 'inicio'),
    path('register/', views.register_page, name = 'register'),
    path('logout/', views.logout_user, name = 'logout'),
    path('editar-perfil/', views.editarPerfil, name = 'editar_perfil'),
    path('user_list/', views.user_list, name='user_list'),
    path('user/<int:user_id>/edit_permissions/', views.edit_user_permissions, name='edit_user_permissions'),


]
