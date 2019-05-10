from django.shortcuts import render
from .models import Project, Website, ArtAlbum, ArtObject

# Create your views here.

def overview(request):
    context = {}
    websites = Website.objects.all()
    art_albums = ArtAlbum.objects.all()
    context['websites'] = websites
    context['albums'] = art_albums 
    
    return render(request, "projects.html", context)

def view_album(request, slug):
    album = ArtAlbum.objects.get(slug=slug)
    objects = ArtObject.objects.all().filter(album=album).distinct()

    context = {
        'album':'album',
        'objects':objects,
    }
    return render(request, "album.html", context)
