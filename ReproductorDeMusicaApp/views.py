from django.shortcuts import render

from .models import LisaMusica, Genero

# Create your views here.

def home(request):
    lista_musica = LisaMusica.objects.all()
    return render(request, 'App de Musica.html', {'li_musica':lista_musica} )


def reproductor(request, id_musica):
    musica_id = LisaMusica.objects.filter(id= id_musica)
    lista_musica = LisaMusica.objects.all()
    list_genero = Genero.objects.all()
    return render(request, 'reproductor.html', {'li_musica':lista_musica, "id_musica":id_musica, "list_genero":list_genero} )

def login(request):
    return render(request, 'login.html' )

def genero(request):
    list_genero = Genero.objects.all()
    lista_musica = LisaMusica.objects.all()
    return render(request, "Genero.html", {"list_genero":list_genero,'li_musica':lista_musica,})


def porGenero(request, genero_id):
    idgenero = Genero.objects.filter(id= genero_id)
    lista_musica = LisaMusica.objects.all()
    return render(request, 'por_genero.html',{'li_musica':lista_musica,"porgenero":genero_id, 'genero':idgenero})