from django.shortcuts import render

from .models import LisaMusica

# Create your views here.

def home(request):
    lista_musica = LisaMusica.objects.all()
    return render(request, 'App de Musica.html', {'li_musica':lista_musica} )


def reproductor(request, id_musica):
    musica_id = LisaMusica.objects.filter(id= id_musica)
    lista_musica = LisaMusica.objects.all()
    return render(request, 'reproductor.html', {'li_musica':lista_musica, "id_musica":id_musica} )

def login(request):
    return render(request, 'login.html' )