from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError

from .models import About
from .forms import ContactForm


# Create your views here.

def index_view(request):
    context = {}
    return render(request, "index.html", context)


def about_view(request):
    context = {}

    try:
        about = About.objects.first()
    except: 
        pass

    context["about"] = about

    return render(request, "about.html",context)

def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            assunto = form.cleaned_data['assunto']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            relay= '''Enviado por: %s\n via %s
            Assunto: %s\n
            Mensagem:
            %s
            '''%(nome, email, assunto, mensagem)
            try:
                send_mail(assunto, relay, settings.EMAIL_HOST_USER, ['pauloroberto.21s@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "contato.html", {'form': form})

def thanks(request):
    return render(request, 'obrigado.html')
