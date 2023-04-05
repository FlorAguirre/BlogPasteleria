from django import forms
from .models import Article, Category, Product, Comment


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
    image = forms.ImageField(required=False)

    class Meta:
        model= Article
        fields = (
            'title',
            'content',
            'public',
            'categories', 
            'image',
        )


class CatForm(forms.ModelForm):

    class Meta:
        model= Category
        fields = (
            'name',
            'description',
            
        )


class ProdForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model= Product
        fields = (
            'name',
            'description',
            'price',
            'image',
            
        )


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 8, 'cols':100, 'placeholder': 'Ingresa tu comentario aquí'}))

    class Meta:
        model = Comment
        fields = ('content',)