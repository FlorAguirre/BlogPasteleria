from django import forms
from .models import Article, Category, Product

class FormArticle(forms.Form):

     title = forms.CharField(
         label = "Título",
         max_length= 40
     )

     content = forms.CharField(
         label = "Contenido",
         widget= forms.Textarea
    )
    
     public_options = [
         (1,'Si'),
         (0,'No')
     ]

     public = forms.TypedChoiceField(
         label = "Publicar?",
         choices = public_options
    )


class ArtForm(forms.ModelForm):

    class Meta:
        model= Article
        fields = (
            'title',
            'content',
            'public',
            'categories',
        )


class CatForm(forms.ModelForm):

    class Meta:
        model= Category
        fields = (
            'name',
            'description',
            
        )


class ProdForm(forms.ModelForm):

    class Meta:
        model= Product
        fields = (
            'name',
            'description',
            'price',
            
        )
