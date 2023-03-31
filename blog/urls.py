from django.urls import path
from . import views

urlpatterns = [
    

    path('articulos/', views.articles, name = 'list_articles'),
    path('categoria/<int:category_id>', views.category, name = 'category'),
    path('articulo/<int:article_id>', views.article, name = 'article'),
    path('save-article/', views.save_article, name = 'save'),
    #path('create-article/', views.RecetaCreateView.as_view(), name = 'create'),
    path('create-full-article/', views.create_full_article, name = 'create_full'),
    path('buscar-articulo/', views.busqueda_articulo, name = 'buscar_articulo'),
    path('buscar/', views.buscar, name= 'buscar'),
    path('categorias/', views.categories, name = 'list_categorias'),
    path('create-category/', views.create_category, name= 'create_category'),
    path('productos/', views.products, name= 'list_productos'),
    path('create_product/', views.create_product, name= 'create_product'),
    path('product/<int:product_id>', views.product, name = 'product'),
    path('buscar-producto/', views.busqueda_producto, name = 'buscar_producto'),
    path('buscarP/', views.buscar_p, name= 'buscarP'),
]
