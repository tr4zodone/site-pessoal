from django.urls import path
from .views import index_view, about_view, email, thanks, english_view

urlpatterns = [
    path("", index_view, name="index"),
    path('sobre', about_view, name="about"),
    path('english', english_view, name="english"),
    path('contato', email, name='contato'),
    path("obrigado", thanks, name="thanks"),
]
