from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255,verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    
    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(default = 'null', verbose_name='Imagen',upload_to="articles")
    public = models.BooleanField(verbose_name='Publicado?')
    #user = models.ForeignKey(User, editable = False, verbose_name= 'Usuario', on_delete = models.CASCADE) # Se borra el registro que esta vinculado con el usuario - on_delete = models.CASCADE
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    categories = models.ManyToManyField(Category, verbose_name='Categorías', blank= True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now= True, verbose_name='Editado el')
    likes_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        ordering = ['-created_at']

    
    def __str__(self):
        return self.title
    


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255,verbose_name='Descripción')
    price = models.IntegerField(default = 0, verbose_name='Precio')
    image = models.ImageField(default = 'null', verbose_name='Imagen',upload_to="products")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-created_at']

    
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-created_on']

    
    def __str__(self):
        return self.content


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class CommentProducto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comentario Producto'
        verbose_name_plural = 'Comentarios Producto'
        ordering = ['-created_on']

    
    def __str__(self):
        return self.content