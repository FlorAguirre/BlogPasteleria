from django.shortcuts import render
from blog.models import Category, Article
from django.shortcuts import render,HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request,'mainapp/index.html',{
        'title' : 'Inicio'
    })

def about(request):
    return render(request,'mainapp/about.html',{
        'title' : 'Sobre nosotros'
    })

