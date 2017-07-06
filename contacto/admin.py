# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from contacto.models import Contacto

class ContactoAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombres', 'apellidos', 'telefono')
		

admin.site.register(Contacto,ContactoAdmin)
# Register your models here.
