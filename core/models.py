from django.db import models

# Create your models here.

from django.conf import settings
from django.contrib.auth.models import AbstractUser

from datetime import datetime, timedelta    

rol_choise = (
    ('A','Addministrador'),
    ('B','Bibliotecario'),
    ('E','Estudiante'),
    ('Em','Empleado'),
)

material_choise = (
    ('A','Audio visual'),
    ('L','Libro'),
    ('R','Revista'),
)

genero_choise = (
    ('A','asesinato'),
    ('AN','angustia'),
    ('AV','aventuras'),
    ('CF','ciencia ficción'),
    ('CH','cuentos de hadas'),
    ('G','gótica'),
    ('P','policíaca'),
    ('PA','paranormal'),
    ('DI','distópica'),
    ('FA','fantástica'),
)

facultad_choice = (
	('A','Artes y Humanidades'),
	('I','Ingeniería'),
    ('C', 'Ciencias Exactas'),
    ('E', 'Ciencias Economicas'),
)

class libro(models.Model):
    titulo = models.CharField(max_length=100)
    material = models.CharField(choices=material_choise, max_length=1)
    slug = models.SlugField()
    descripción = models.TextField()
    imagen = models.ImageField()

    def __str__(self):
        return self.titulo

class autor(models.Model):
    libro = models.ForeignKey(libro, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=40, blank=True)
    cuidadOrigen = models.CharField(max_length=100,blank=True)
    nacimiento = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre

class genero(models.Model):
    libro = models.ForeignKey(libro,on_delete=models.CASCADE)
    genero = models.CharField(choices=genero_choise, max_length=3)
    
    def __str__(self):
        return self.genero
 
class editorial(models.Model):
    libro = models.ForeignKey(libro,on_delete=models.CASCADE)
    editorial = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.editorial

class CustomUser(AbstractUser):
    documento = models.CharField(max_length=20, blank=False, null=False)
    telefono = models.CharField(max_length=20, blank=False, null=False)
    direccion = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.documento
    
class prestamo(models.Model):
    libro = models.ForeignKey(libro ,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(default=datetime.now() + timedelta(days=30))
    

    def __str__(self):
        return str(self.pk)
    
