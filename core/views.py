from django.shortcuts import render

from django.db.models import Q, Count

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.views.generic.edit import FormView

from django.views.generic import ListView, DetailView

from .forms import CustomUserCreationForm
from .models import prestamo, CustomUser, libro, autor, genero

from .filters import filtrolibros

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def PrestamoView(request):
    template_name = 'prestamo.html'
    return render(request, template_name)

def DevolucionView(request):
    template_name = 'devolucion.html'
    return render(request, template_name)

def home (request):
    prestamos = prestamo.objects.all()
    libros = libro.objects.all()
    template_name = 'home.html'
    context = {'prestamos': prestamos,'libros': libros} #Importante ya lo sabes#
    return render(request, template_name, context)

def detalleslug(request, slug):
    libros = libro.objects.get(slug=slug)
    autors = autor.objects.all()
    template_name = 'libro.html'
    context = {"libros": libros, "autors": autors}
    return render(request, template_name, context)

class Detallesbusqueda(ListView):
    model = libro
    template_name = 'busqueda.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = filtrolibros(self.request.GET,  queryset=self.get_queryset())
        return context

def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request):
    qs = libro.objects.all()
    title_contains_query = request.GET.get('title_contains')
    autor_contains_query = request.GET.get('name_contains')
    material_contains = request.GET.get('material_contains')
    
    if material_contains != None:
        qs = qs.filter(material__icontains=material_contains)

    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(titulo__icontains=title_contains_query)
            
    elif is_valid_queryparam(autor_contains_query):
        qs = qs.filter(Q(titulo__icontains=autor_contains_query)
                | Q(autor__nombre__icontains=autor_contains_query)
                ).distinct()
                        
    return qs

def BootstrapFilterView(request):
    submitbutton= request.GET.get('order_contains')
    
    if submitbutton=="order_contains":
        qs = filter(request).order_by('titulo')
    else:
        qs = filter(request)

    autors = autor.objects.all()
    context = {
        'queryset': qs,
        'autors' : autors,
    }
    return render(request, "busqueda.html", context)