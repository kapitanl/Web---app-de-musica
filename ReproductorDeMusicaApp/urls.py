from django.urls import path
from .views import home, login, reproductor, genero, porGenero
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', home, name='home'),
    path('login/', login,  name='login'),
    path('reproductor/<int:id_musica>', reproductor,  name='reproductor'),
    path('gener/', genero, name= 'genero' ),
    path('porgenero/<int:genero_id>', porGenero, name= 'porGenero' )
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)