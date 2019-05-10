from django.contrib import admin
from .models import Website, ArtAlbum, ArtObject, Project 

# Register your models here.
admin.site.register(Website)
admin.site.register(ArtAlbum)
admin.site.register(ArtObject)
