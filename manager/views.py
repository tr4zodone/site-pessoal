from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Channel, Resource, Category

# Create your views here.

class ManagerView(TemplateView): 
    template_name = "manager.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chans'] = Channel.objects.all().order_by('initials')
        context['resources'] = Resource.objects.all().order_by("name").filter(category__isnull=False)
        context['categories'] = Category.objects.all().order_by("title")

        return context
    

