from django.contrib import admin
from .models import Category, Article, Product


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name'),
    readonly_fields = ('created_at'),
    

class ArticleAdmin(admin.ModelAdmin):
    autocomplete_fields = ['categories']


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at'),

# class ArticleAdmin(admin.ModelAdmin):
#      readonly_fields = ('user','created_at', 'updated_at')

# Para que se pueda mostrar el usuario, sin tener que editarlo. Que tome el usuario que haya iniciado sesión como creador del artículo

# def save_model(self,request, obj, form, change):
#         if not obj.user_id:
#             obj.user_id = request.user.id
        
#         obj.save()



# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Product, ProductAdmin)

