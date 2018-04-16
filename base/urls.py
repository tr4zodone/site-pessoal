from django.urls import path
from .views import index_view, about_view, email, thanks

urlpatterns = [
    path("", index_view, name="index"),
    path('sobre', about_view, name="about"),
    path('contato', email, name='contato'),
    path("obrigado", thanks, name="thanks"),
]
