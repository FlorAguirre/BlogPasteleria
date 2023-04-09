from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Category, Article, Product, Like
from django.shortcuts import render,HttpResponse, redirect
from blog.forms import ArtForm, CatForm, ProdForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from blog.forms import CommentForm,CommentFormProducto
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from mainapp.models import Avatar


# Create your views here.

#######  LISTAR RECETAS, CATEGORIAS Y PRODUCTOS #######


def articles(request):

    # Sacar articulos
    articles = Article.objects.all()
    # Paginar los articulos
    paginator = Paginator(articles, 2)

    # Recoger numero pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    
    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request,'articles/list.html',{
        'title' : 'Artículos',
        'articles' : page_articles,
        'url' : avatares[0].imagen.url
        
    })


def categories(request):

    categories = Category.objects.all()

    avatares = Avatar.objects.filter(user=request.user.id)
    


    
    return render(request,'categories/listcategory.html',{
        'title' : 'Categorías',
        'categories' : categories,
        'url' : avatares[0].imagen.url
    })

def products(request):

    products = Product.objects.all()

     # Paginar los articulos
    paginator = Paginator(products, 2)

    page = request.GET.get('page')
    page_products = paginator.get_page(page)


    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request,'products/listproducts.html',{
        'title' : 'Productos',
        'products' : page_products,
        'url' : avatares[0].imagen.url
    })

def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(categories = category_id)
    avatares = Avatar.objects.filter(user=request.user.id)
    paginator = Paginator(articles, 2)

    page = request.GET.get('page')
    page_categories = paginator.get_page(page)
    
    return render(request,'categories/category.html',{
        'category' : category,
        'articles' :page_categories,
        'url' : avatares[0].imagen.url
    })

def article(request, article_id):

    article = get_object_or_404(Article, id =article_id)
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'articles/detail.html',{
        'article' : article,
        'url' : avatares[0].imagen.url
        
   })


def like_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    try:
        # Si el usuario ya dio like a este artículo, eliminar su like
        like = Like.objects.get(article=article, author=user)
        like.delete()
    except Like.DoesNotExist:
        # Si el usuario no ha dado like todavía, crear uno nuevo
        like = Like.objects.create(article=article, author=user)
    return HttpResponseRedirect(reverse('article', args=[article.id]))


def product(request, product_id):

    product = get_object_or_404(Product, id =product_id)
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'products/detail.html',{
        'product' : product,
        'url' : avatares[0].imagen.url
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
@login_required

def create_full_article(request):
    articulo = None # Crear la variable articulo fuera del bloque condicional
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":
        formulario = ArtForm(request.POST,request.FILES)
        if formulario.is_valid():
            # Extraer los campos del formulario
            title = formulario.cleaned_data.get('title')
            content = formulario.cleaned_data.get('content')
            public = formulario.cleaned_data.get('public')
            category_ids = request.POST.getlist('categories') # obtener la lista de los ids de categorías seleccionadas
            categories = Category.objects.filter(id__in=category_ids)
            image = formulario.cleaned_data.get('image')
  

            # Crear el articulo
            articulo = Article(
                title = title,
                content = content,
                public = public,
                image = image,
                author =request.user
            )
            articulo.save()
            articulo.categories.set(categories)

            # Crear mensaje flash (sesión que solo se muestra 1 vez)
            messages.success(request,f'Se ha guardado correctamente la receta: {articulo.title}')
            return redirect('list_articles')
    else:
        formulario = ArtForm()
    return render(request, 'articles/create_full_article.html',{
        'form' : formulario,
        'url' : avatares[0].imagen.url
    })


def create_category(request):
    categoria = None # Crear la variable articulo fuera del bloque condicional
    avatares = Avatar.objects.filter(user=request.user.id)
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
        'form' : formulario,
        'url' : avatares[0].imagen.url})



def create_product(request):
    producto = None # Crear la variable articulo fuera del bloque condicional
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":
        formulario = ProdForm(request.POST,request.FILES)
        if formulario.is_valid():
            # Extraer los campos del formulario
            name = formulario.cleaned_data.get('name')
            description = formulario.cleaned_data.get('description')
            price = formulario.cleaned_data.get('price')
            image = formulario.cleaned_data.get('image')

  

            # Crear el articulo
            producto = Product(
                name = name,
                description = description,
                price = price,
                image = image,
                author =request.user
              
                
            )
            producto.save()
           

            # Crear mensaje flash (sesión que solo se muestra 1 vez)
            messages.success(request,f'Se ha guardado correctamente el producto: {producto.name}')
            return redirect('list_productos')
    else:
        formulario = ProdForm()
    return render(request, 'products/create_product.html',{
        'form' : formulario,
        'url' : avatares[0].imagen.url
    })




#######  BUSCAR RECETA Y PRODUCTO #######

def busqueda_articulo(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request,'articles/buscar_articulo.html',{'url' : avatares[0].imagen.url })



def buscar(request):

    if request.POST['title']:

        articulo = request.POST['title']
        articulos = Article.objects.filter(title__icontains= articulo)
        avatares = Avatar.objects.filter(user=request.user.id)

        return render(request,"articles/resultados_busqueda.html",{"articulos":articulos,'url' : avatares[0].imagen.url })
    
    else:
        respuesta = "No enviaste datos"


    return HttpResponse(respuesta)
    

def busqueda_producto(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request,'products/buscar_producto.html',{'url' : avatares[0].imagen.url })



def buscar_p(request):

    if request.POST['name']:

        producto = request.POST['name']
        productos = Product.objects.filter(name__icontains= producto)
        avatares = Avatar.objects.filter(user=request.user.id)

        return render(request,"products/resultados_busquedaP.html",{"productos":productos,'url' : avatares[0].imagen.url })
    
    else:
        respuesta = "No enviaste datos"


    return HttpResponse(respuesta)
    

@login_required

def modificar_articulo(request, id):

    articulo = get_object_or_404(Article, id = id)

    data = {
        'form' : ArtForm(instance= articulo)
    }

    avatares = Avatar.objects.filter(user=request.user.id)

     # Verificar si el usuario actual es el autor del artículo
    if request.user != articulo.author and not request.user.is_superuser:
        # Si el usuario actual no es el autor del artículo, redirigir a la página de inicio
        messages.error(request, 'Solo el autor del artículo puede editarlo o eliminarlo')
        return redirect('inicio')

    if request.method == 'POST':
        formulario = ArtForm(data = request.POST, instance = articulo, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "La receta ha sido modificada")
            return redirect('list_articles')
        
        data['form'] = formulario
       
    return render(request, 'articles/modificar.html',{
        'form': ArtForm(instance=articulo),
        'url': avatares[0].imagen.url
    })



@login_required

def modificar_producto(request, id):

    producto = get_object_or_404(Product, id = id)

    data = {
        'form' : ProdForm(instance= producto)
    }

    avatares = Avatar.objects.filter(user=request.user.id)
     # Verificar si el usuario actual es el autor del artículo
    if request.user != producto.author and not request.user.is_superuser:
        # Si el usuario actual no es el autor del artículo, redirigir a la página de inicio
        messages.error(request, 'Solo el autor del producto puede editarlo o eliminarlo')
        return redirect('inicio')

    if request.method == 'POST':
        formulario = ProdForm(data = request.POST, instance = producto, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "La receta ha sido modificada")
            return redirect('list_productos')
        
        data['form'] = formulario
    return render(request, 'products/modificar.html', {
        'form' : ProdForm(instance= producto),
        'url': avatares[0].imagen.url

    })



# @user_passes_test(is_staff)
# def eliminar_articulo(request, id):
#     articulo = get_object_or_404(Article, id = id)
#     articulo.delete()
#     messages.success(request, "La receta ha sido eliminada")
#     return redirect('list_articles')

def eliminar_articulo(request, id):
    articulo = get_object_or_404(Article, id = id)
     # Verificar si el usuario actual es el autor del artículo
    if request.user != articulo.author  and not request.user.is_superuser:
        # Si el usuario actual no es el autor del artículo, redirigir a la página de inicio
        messages.error(request, 'Solo el autor del artículo puede editarlo o eliminarlo')
        return redirect('inicio')
    
    articulo = get_object_or_404(Article, id=id)
    articulo.delete()
    messages.success(request, "La receta ha sido eliminada")
    return redirect('list_articles')



def eliminar_producto(request, id):
    producto = get_object_or_404(Product, id = id)
     # Verificar si el usuario actual es el autor del artículo
    if request.user != producto.author  and not request.user.is_superuser:
        # Si el usuario actual no es el autor del artículo, redirigir a la página de inicio
        messages.error(request, 'Solo el autor del producto puede editarlo o eliminarlo')
        return redirect('inicio')
    
    producto = get_object_or_404(Product, id=id)
    producto.delete()
    messages.success(request, "El producto ha sido eliminado")
    return redirect('list_productos')


# Agregar comentarios en Recetas

@login_required
def crear_comentario(request, article_id):
    article = Article.objects.get(id=article_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            messages.success(request, 'Tu comentario ha sido agregado')
            return redirect('article', article_id=article_id)
    else:
        form = CommentForm()

    context = {
        'article': article,
        'form': form
    }

    return render(request, 'articles/agregar_comentario.html', context)



# Agregar Comentarios en Productos

@login_required
def crear_comentario_producto(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = CommentFormProducto(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.author = request.user
            comment.save()
            messages.success(request, 'Tu comentario ha sido agregado')
            return redirect('product', product_id=product_id)
    else:
        form = CommentFormProducto()

    context = {
        'product': product,
        'form': form
    }

    return render(request, 'products/agregar_comentario.html', context)

