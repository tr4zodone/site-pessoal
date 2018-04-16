from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ManagerView(TemplateView): 
    template_name = "manager.html"

