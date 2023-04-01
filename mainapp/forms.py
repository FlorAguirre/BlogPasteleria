from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

  


class UserEditForm(UserChangeForm):
    email = forms.EmailField(label="Modificar E-mail")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email','last_name', 'first_name']
        help_texts = {k:"" for k in fields}

    def clean_password(self):
        return make_password(self.cleaned_data["password"])