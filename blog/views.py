from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article, Product
from django.shortcuts import render,HttpResponse, redirect
from blog.forms import ArtForm, CatForm, ProdForm
from django.contrib import messages





# Create your views here.

#######  LISTAR RECETAS, CATEGORIAS Y PRODUCTOS #######


def articles(request):

    articles = Article.objects.all()
    
    return render(request,'articles/list.html',{
        'title' : 'Artículos',
        'articles' : articles,
    })


def categories(request):

    categories = Category.objects.all()
    
    return render(request,'categories/listcategory.html',{
        'title' : 'Categorías',
        'categories' : categories,
    })

def products(request):

    products = Product.objects.all()
    
    return render(request,'products/listproducts.html',{
        'title' : 'Productos',
        'products' : products,
    })

def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(categories = category_id)

    
    return render(request,'categories/category.html',{
        'category' : category,
        'articles' :articles
    })

def article(request, article_id):

    article = get_object_or_404(Article, id =article_id)

    return render(request, 'articles/detail.html',{
        'article' : article
    })


def product(request, product_id):

    product = get_object_or_404(Product, id =product_id)

    return render(request, 'products/product.html',{
        'product' : product
    })



# def crear_articulo(request,title,content,public):
#     articulo = Article(
#         title = title,
#         content = content,
#         public = public
#     )

#######  GUARDAR RECETA #######


def save_article(request):

    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']
    




        articulo = Article(
            title = title,
            content = content,
            public = public,

           
          
        )

        articulo.save()
        return HttpResponse(f'Receta creada:<strong>{articulo.title}')
    
    else:
        return HttpResponse("<h2> No se ha podido crear la receta</h2>")

    

# def create_article(request):

#     return render(request,'articles/create_article.html')

# #######  CREAR RECETA, CATEGORIA Y PRODUCTO #######

def create_full_article(request):
    articulo = None # Crear la variable articulo fuera del bloque condicional
    if request.method == "POST":
        formulario = ArtForm(request.POST)
        if formulario.is_valid():
            # Extraer los campos del formulario
            title = formulario.cleaned_data.get('title')
            content = formulario.cleaned_data.get('content')
            public = formulario.cleaned_data.get('public')
            category_ids = request.POST.getlist('categories') # obtener la lista de los ids de categorías seleccionadas
            categories = Category.objects.filter(id__in=category_ids)

  

            # Crear el articulo
            articulo = Article(
                title = title,
                content = content,
                public = public,
                
            )
            articulo.save()
            articulo.categories.set(categories)

            # Crear mensaje flash (sesión que solo se muestra 1 vez)
            messages.success(request,f'Se ha guardado correctamente la receta: {articulo.title}')
            return redirect('list_articles')
    else:
        formulario = ArtForm()
    return render(request, 'articles/create_full_article.html',{
        'form' : formulario
    })


def create_category(request):
    categoria = None # Crear la variable articulo fuera del bloque condicional
    if request.method == "POST":
        formulario = CatForm(request.POST)
        if formulario.is_valid():
            # Extraer los campos del formulario
            name = formulario.cleaned_data.get('name')
            description = formulario.cleaned_data.get('description')
            
           

  

            # Crear el articulo
            categoria = Category(
                name = name,
                description = description,
              
                
            )
            categoria.save()
           

            # Crear mensaje flash (sesión que solo se muestra 1 vez)
            messages.success(request,f'Se ha guardado correctamente la categoría: {categoria.name}')
            return redirect('list_categorias')
    else:
        formulario = CatForm()
    return render(request, 'categories/create_category.html',{
        'form' : formulario
    })



def create_product(request):
    producto = None # Crear la variable articulo fuera del bloque condicional
    if request.method == "POST":
        formulario = ProdForm(request.POST)
        if formulario.is_valid():
            # Extraer los campos del formulario
            name = formulario.cleaned_data.get('name')
            description = formulario.cleaned_data.get('description')
            price = formulario.cleaned_data.get('price')
           

  

            # Crear el articulo
            producto = Product(
                name = name,
                description = description,
                price = price
              
                
            )
            producto.save()
           

            # Crear mensaje flash (sesión que solo se muestra 1 vez)
            messages.success(request,f'Se ha guardado correctamente el producto: {producto.name}')
            return redirect('list_productos')
    else:
        formulario = ProdForm()
    return render(request, 'products/create_product.html',{
        'form' : formulario
    })




#######  BUSCAR RECETA Y PRODUCTO #######

def busqueda_articulo(request):
    return render(request,'articles/buscar_articulo.html')



def buscar(request):

    if request.POST['title']:

        articulo = request.POST['title']
        articulos = Article.objects.filter(title__icontains= articulo)

        return render(request,"articles/resultados_busqueda.html",{"articulos":articulos})
    
    else:
        respuesta = "No enviaste datos"


    return HttpResponse(respuesta)
    

def busqueda_producto(request):
    return render(request,'products/buscar_producto.html')



def buscar_p(request):

    if request.POST['name']:

        producto = request.POST['name']
        productos = Product.objects.filter(name__icontains= producto)

        return render(request,"products/resultados_busquedaP.html",{"productos":productos})
    
    else:
        respuesta = "No enviaste datos"


    return HttpResponse(respuesta)
    

