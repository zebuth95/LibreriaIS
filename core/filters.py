import django_filters
from .models import libro

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class filtrolibros(django_filters.FilterSet):

    class Meta:
        model = libro 
        fields = {
            'titulo':['icontains'],
        }
