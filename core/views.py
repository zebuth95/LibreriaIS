from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from .models import prestamo, CustomUser, libro

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def busqueda (request):
    prestamos = prestamo.objects.all()
    libros = libro.objects.all()
    template_name = 'test.html'
    context = {'prestamos': prestamos,'libros': libros} #Importante ya lo sabes#
    return render(request, template_name, context)

def detalleslug(request, slug):
    libros = libro.objects.get(slug=slug)
    template_name = 'test.html'
    context = {"libros": libros}
    return render(request, template_name, context)

