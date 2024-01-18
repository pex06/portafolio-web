from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        asunto = f"De: {email} - Portafolio Web"
        remitente = 'marianpetrut270@gmail.com'

        send_mail(asunto, mensaje, remitente, ['marianpetrut270@gmail.com'])

        return HttpResponse('Correo enviado con éxito :)')
    else:
        return HttpResponse('Error en el formulario :(')

