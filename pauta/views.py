# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.
class InicioView(TemplateView):
	template_name= "pauta/templates/pauta/index.html"
	