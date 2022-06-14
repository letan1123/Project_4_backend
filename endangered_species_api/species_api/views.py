from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import SpeciesSerializer
from .models import Species

class SpeciesList(generics.ListCreateAPIView):
    queryset = Species.objects.all().order_by('id')
    serializer_class = SpeciesSerializer

class SpeciesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Species.objects.all().order_by('id')
    serializer_class = SpeciesSerializer
