from .models import *
from rest_framework import viewsets
from adopcionperros.serializers import MascotaSerializer

class MascotaViewSet( viewsets.ModelViewSet ):
    queryset = Mascotas.objects.all().order_by( 'FechaPublicado' )
    serializer_class = MascotaSerializer