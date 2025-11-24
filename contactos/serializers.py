from rest_framework import serializers
from .models import Contacto
#formato JSON
class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'#todos los campos del modelo