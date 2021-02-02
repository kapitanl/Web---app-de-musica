from django.db import models

# Create your models here.

class Genero(models.Model):
    nombre_genero= models.CharField(max_length=100)
    
    class Meta:
        verbose_name='Genero'
        verbose_name_plural='Generos'
    
    def __str__(self):
        return self.nombre_genero

class LisaMusica(models.Model):
    nombre_cancion= models.CharField(max_length=100)
    url_musica= models.CharField(max_length=200)
    imagen= models.ImageField(upload_to='imgMusica')
    categoria = models.CharField(null=True, max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name='LisaMusica'
        verbose_name_plural='LisasMusicas'
    
    def __str__(self):
        return self.nombre_cancion