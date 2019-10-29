from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.views.generic import ListView, DetailView

from .forms import CustomUserCreationForm
from .models import prestamo, CustomUser, libro, portada

from .filters import filtrolibros

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def home (request):
    prestamos = prestamo.objects.all()
    libros = libro.objects.all()
    template_name = 'home.html'
    context = {'prestamos': prestamos,'libros': libros} #Importante ya lo sabes#
    return render(request, template_name, context)

def detalleslug(request, slug):
    libros = libro.objects.get(slug=slug)
    template_name = 'home.html'
    context = {"libros": libros}
    return render(request, template_name, context)

def busqueda (request):
    libros = libro.objects.all()
    template_name = 'busqueda.html'
    context = {'libros': libros}
    return render(request, template_name, context)

class Detallesbusqueda(ListView):
    model = libro
    template_name = 'busqueda.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = filtrolibros(self.request.GET,  queryset=self.get_queryset())
        return context
