from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.login_page, name = 'login'),
    path('inicio/', views.index, name = 'inicio'),
    path('register/', views.register_page, name = 'register'),
    path('logout/', views.logout_user, name = 'logout'),

]
