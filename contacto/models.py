# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contacto(models.Model):
	"""docstring for contacto"""

	nombres = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	email = models.EmailField(max_length=40)
	telefono = models.CharField (max_length=12)
	direccion = models.CharField(max_length=30)
    
        

"""
class Movie(models.Model):
    name = models.CharField(max_length=144)
    description = models.TextField()
    anio = models.PositiveIntegerField()
    category = models.ForeignKey(Category)
    sort_order = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True) 
    """