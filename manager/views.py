from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from .models import Channel, Resource, Category
from .forms import ResourceForm
import json

# Create your views here. 

def manager_view(request):
    manager_template = "manager.html"
    context = {}
    context['chans'] = Channel.objects.all().order_by('initials')
    context['resources'] = Resource.objects.all().order_by("name").filter(category__isnull=False)
    context['categories'] = Category.objects.all().order_by("title").filter(resource__isnull=False).distinct()
    context["form"] = ResourceForm()

    if request.method == "POST":
        name = request.POST.get("name")
        url = request.POST.get("url")
        category = request.POST.get("category")

        response_data = {}
        
        categories = Category.objects.all()
        catlen = list(range(1, len(categories) + 1)) # length of categories queryset
        catzip = [x for x in zip(catlen, categories)] #joining each category with is index
        category = catzip[int(category) - 1][1]
        
        if not "http" in url:
            url = "http://" + url

        form = Resource(name=name, url=url, category=category)

        form.save()


        response_data['name'] = form.name
        response_data['url'] = form.url
        response_data['category'] = category.title

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    return render(request, manager_template, context)
