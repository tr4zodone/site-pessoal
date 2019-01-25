from django import forms
from .models import Category, Resource

class ResourceForm(forms.ModelForm):
    name = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    url = forms.URLField(label="URL", widget=forms.TextInput(attrs={'placeholder': 'URL'}))

    class Meta():
        model = Resource
        fields = ("name", "url", "category")

        use_required_attribute = False
