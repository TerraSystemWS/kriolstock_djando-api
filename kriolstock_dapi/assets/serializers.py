from rest_framework import serializers
from assets.models import Documento

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        # fields = '__all__'
        fields = ['title', 'description', 'image_url', 'price', 'visibility', 'status', 'user']

