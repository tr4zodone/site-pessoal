from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    assunto = forms.CharField(required=True)
    mensagem = forms.CharField(widget=forms.Textarea)
