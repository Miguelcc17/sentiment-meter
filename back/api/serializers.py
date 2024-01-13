from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nombre', 'correo_electronico', 'contraseña')

class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos
        fields = ('id', 'texto', 'sentimiento', 'emoción', 'usuario')