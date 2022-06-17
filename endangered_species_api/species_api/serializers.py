from rest_framework import serializers
from .models import Species

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ('id', 'commonName', 'species', 'order', 'genus', 'habitat', 'diet', 'image', 'level', 'description')
