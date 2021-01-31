from django.urls import path
from .views import home, login, reproductor
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', home, name='home'),
    path('login/', login,  name='login'),
    path('reproductor/<int:id_musica>', reproductor,  name='reproductor'),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)