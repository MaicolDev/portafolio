from django.db import models
from django import forms
from django.db.models.fields import CharField,EmailField,TextField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.

class Proyecto(models.Model):
    titulo= CharField(max_length=100)
    descripcion= CharField(max_length=250)
    imagen= ImageField(upload_to='media')
    url= URLField(blank=True)

class Contacto(models.Model):
    nombre=CharField(max_length=20)
    apellido=CharField(max_length=20)
    email=EmailField()
    mensaje=TextField()
