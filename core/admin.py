from django.contrib import admin

# Register your models here.

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import libro, portada, autor, genero, editorial, prestamo, CustomUser

class CustomUserAdmin(UserAdmin):   #new
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email','documento','telefono','direccion']

class Customprestamo(admin.ModelAdmin):   #new
    model = prestamo
    list_display = ['fecha_prestamo','get_user','get_libro','fecha_devolucion','cantidad']

    #para elementos relacionados
    def get_libro(self, obj):
        return obj.libro.titulo
    get_libro.admin_order_field  = 'titulo'  #Allows column order sorting
    get_libro.short_description = 'Libro'  #Renames column head

    def get_user(self, obj):
        return obj.user.documento
    get_user.admin_order_field  = 'documento'  #Allows column order sorting
    get_user.short_description = 'Documento usuario'  #Renames column head

class Customportada(admin.ModelAdmin):   #new
    model = portada
    list_display = ['portada_id','nombre']

class Customautor(admin.ModelAdmin):   #new
    model = autor
    list_display = ['get_pk','nombre','get_titulo']

    #para elementos relacionados
    def get_pk(self, obj):
        return obj.libro.pk
    get_pk.admin_order_field  = 'pk'  #Allows column order sorting
    get_pk.short_description = 'ID'  #Renames column head

    def get_titulo(self, obj):
        return obj.libro.titulo
    get_titulo.admin_order_field  = 'titulo'  #Allows column order sorting
    get_titulo.short_description = 'Libro'  #Renames column head

class Customlibro(admin.ModelAdmin):
    model = libro
    list_display = ['pk','titulo']


admin.site.register(autor, Customautor)
admin.site.register(portada, Customportada)
admin.site.register(libro,Customlibro)
admin.site.register(genero)
admin.site.register(editorial)

admin.site.register(prestamo, Customprestamo)

admin.site.register(CustomUser, CustomUserAdmin) #new