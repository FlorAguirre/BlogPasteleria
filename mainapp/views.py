from django.shortcuts import render,redirect
from django.contrib import messages
from blog.models import Category, Article
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm
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

# Create your views here.


@login_required(login_url = 'login')
def index(request):
    return render(request,'mainapp/index.html',{
        'title' : 'Inicio'
    })

@login_required(login_url = 'login')
def about(request):
    return render(request,'mainapp/about.html',{
        'title' : 'Sobre nosotros'
    })

def register_page(request):

    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)


        if register_form.is_valid():
            register_form.save()
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
            return render(request, "mainapp/index.html")
    else:
           # Obtener el objeto User actual y pasarlo como instancia del formulario
        miFormulario = UserEditForm(instance=usuario)

        # Actualizar los valores de los campos del formulario
        miFormulario.fields['email'].initial = usuario.email
        miFormulario.fields['last_name'].initial = usuario.last_name
        miFormulario.fields['first_name'].initial = usuario.first_name
    return render(request, "users/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})





@user_passes_test(lambda u: u.is_superuser)
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})