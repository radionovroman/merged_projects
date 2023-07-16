from unicodedata import name
from rest_framework import generics, viewsets
from .models import WorldBorder
from .serializers import WorldBorderSerializer
from django.shortcuts import get_object_or_404
from django.contrib.gis.db.models.functions import Area


class WorldViewSet(viewsets.ModelViewSet):
    queryset = WorldBorder.objects.all()
    serializer_class = WorldBorderSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(WorldBorder, name=item)


class CreateCountry(generics.CreateAPIView):
    queryset = WorldBorder.objects.all()
    serializer_class = WorldBorderSerializer



