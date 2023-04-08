from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.login_page, name = 'login'),
    path('inicio/', views.index, name = 'inicio'),
    path('about/', views.about, name = 'about'),
    path('register/', views.register_page, name = 'register'),
    path('logout/', views.logout_user, name = 'logout'),
    path('editar-perfil/', views.editarPerfil, name = 'editar_perfil'),
    path('perfil/<int:user_id>', views.perfil, name = 'perfil'),
    path('user_list/', views.user_list, name='user_list'),
    path('user/<int:user_id>/edit_permissions/', views.edit_user_permissions, name='edit_user_permissions'),
    path('select-avatar/', views.select_avatar, name='select_avatar'),
    path('buscar-opciones/', views.buscarBase, name='buscar_opciones'),
    path('contactanos/', views.contactanos, name='contactanos'),



]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)