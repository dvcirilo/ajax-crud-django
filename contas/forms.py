from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Usuario

class CadastroForm(UserCreationForm):
    class Meta:
        model = Usuario
        # os campos password e password2 (confirmação) já vem
        # no UserCreationForm
        fields = ['username', 'email'] 

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = "__all__"
