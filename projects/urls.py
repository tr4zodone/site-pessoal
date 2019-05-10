from django.urls import path
from django.conf import settings
from .views import overview, view_album 
from django.conf.urls.static import static

urlpatterns = [
    path("", overview, name="projects"),
    path("3D/<slug:slug>", view_album, name="album_filter"),
]
