from .models import *
from rest_framework import serializers


class MascotaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mascotas
        fields = ('Imagen', 'NombreMascota', 'RazaPredominante', 'Descripcion','Estado', 'FechaPublicado')