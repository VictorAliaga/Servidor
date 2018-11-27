from django.db import models
from django import forms
from django.utils import timezone

# Clase Mascotas
class Mascotas(models.Model):

    # Inicializamos los atributos
    DISPONIBLE = 'Disponible'
    RESCATADO = 'Rescatado'
    ADOPTADO = 'Adoptado'

    # Definimos las Opciones
    STATE_CHOICES = ((DISPONIBLE, 'Disponible'),(RESCATADO, 'Rescatado'),(ADOPTADO, 'Adoptado'))

    Imagen = models.ImageField(upload_to='upload')
    NombreMascota = models.CharField(max_length=20)
    RazaPredominante = models.CharField(max_length=15)
    Descripcion = models.TextField()
    Estado = models.CharField(max_length=10, choices=STATE_CHOICES, default=DISPONIBLE)
    FechaPublicado = models.DateTimeField(blank=True, null=True)
    
    # Comprobamos que la fecha de publicado sea la actual
    def mascota_publicada(self):
        self.FechaPublicado = timezone.now()
        self.save()

    def update(self):
        self.Estado = "Adoptado"
        self.save()     
        
    # Retornamos el nombre de la mascota
    def __str__(self):
        return self.NombreMascota