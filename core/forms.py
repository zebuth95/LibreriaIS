# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label = "email")
    documento = forms.CharField(label = "documento")
    telefono = forms.CharField(label = "telefono")
    direccion = forms.CharField(label = "direccion")

    class Meta:
        model = CustomUser
        fields = ('username','email','documento','telefono','direccion')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username','email','documento','telefono','direccion')