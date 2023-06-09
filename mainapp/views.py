from django.shortcuts import render,redirect
from django.contrib import messages
from blog.models import Category, Article
from mainapp.models import Avatar
from mainapp.forms import RegisterForm, UserEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.conf import settings
import os
from django.core.mail import send_mail

# Create your views here.


from django.contrib.auth.decorators import user_passes_test

def is_active(user):
    return user.is_active

def is_staff(user):
    return user.is_staff





@login_required(login_url = 'login')
def index(request):

    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request,'mainapp/index.html',{
        'title' : 'Inicio',
        "url" : avatares[0].imagen.url
    })

@login_required(login_url = 'login')
def about(request):

    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request,'mainapp/about.html',{
        'title' : 'Sobre nosotros',
        "url" : avatares[0].imagen.url
    })


@login_required(login_url = 'login')
def buscarBase(request):

    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request,'mainapp/buscar.html',{
        'title' : 'Buscar',
        "url" : avatares[0].imagen.url
    })

"""
def register_page(request):
     register_form = RegisterForm()

     if request.method == 'POST':
         register_form = RegisterForm(request.POST,request.FILES)


         if register_form.is_valid():
             register_form.save()
             messages.success(request, "Se ha registrado correctamente")

             return redirect('register')
    

     return render(request,'users/register.html',{
         'title' : 'Registro',
         'register_form' : register_form
     })

"""

def register_page(request):
    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST,request.FILES)

        if register_form.is_valid():
            user = register_form.save()
            # Asignar un avatar por defecto al usuario
            default_avatar = Avatar.objects.get(pk=settings.DEFAULT_AVATAR_ID)
            avatar = Avatar(user=user, imagen=default_avatar.imagen)
            avatar.save()
            # Mostrar un mensaje de éxito
            messages.success(request, "Se ha registrado correctamente")

            return redirect('register')
    
    return render(request,'users/register.html',{
        'title' : 'Registro',
        'register_form' : register_form
    })




def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('inicio')
        
        else:
            messages.warning(request,'Usuario o clave incorrectos')

    return render(request,"users/login.html",{
        "title":"Identificate"
    })


def logout_user(request):
    logout(request)
    return redirect('login')


# Vista de editar el perfil
@login_required(login_url='login')
def editarPerfil(request):
    usuario = request.user
    avatares = Avatar.objects.filter(user=request.user.id)
   
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, instance=usuario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password = informacion['password']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            messages.success(request, "Se ha modificado el usuario correctamente")
            return render(request, "users/perfil.html",{'url' : avatares[0].imagen.url})
    else:
           # Obtener el objeto User actual y pasarlo como instancia del formulario
        miFormulario = UserEditForm(instance=usuario)

        # Actualizar los valores de los campos del formulario
        miFormulario.fields['email'].initial = usuario.email
        miFormulario.fields['last_name'].initial = usuario.last_name
        miFormulario.fields['first_name'].initial = usuario.first_name
    return render(request, "users/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario, 'url' : avatares[0].imagen.url})





@user_passes_test(lambda u: u.is_superuser)
def user_list(request):
    users = User.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'users/user_list.html', {
        'users': users,
        'url' : avatares[0].imagen.url
        })


@login_required
@permission_required('auth.change_user', raise_exception=True)
def edit_user_permissions(request, user_id):
    user = get_object_or_404(User, id=user_id)
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'users/edit_user_permissions.html', {'form': form, 'user': user,'url' : avatares[0].imagen.url})


def perfil(request, user_id):
    user = get_object_or_404(User, id =user_id)
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'users/perfil.html',{
        'user' : user,
        "url" : avatares[0].imagen.url})


@login_required
def select_avatar(request):


    if request.method == 'POST':
        selected_avatar = request.POST.get('avatar')
        if selected_avatar:
            avatar = Avatar.objects.get(user=request.user)
            avatar.imagen = 'avatares/' + selected_avatar
            avatar.save()
            return redirect('perfil', user_id=request.user.id)
    
    avatar_dir = os.path.join(settings.MEDIA_ROOT, 'avatares')
    avatares = os.listdir(avatar_dir)
    avatares_url = Avatar.objects.filter(user=request.user.id)
    context = {'avatares': avatares, "url" : avatares_url[0].imagen.url}
    return render(request, 'users/select_avatar.html', context)

