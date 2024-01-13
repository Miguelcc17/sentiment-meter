from .models import Usuario, Datos
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer, DatosSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer

class DatosViewSet(viewsets.ModelViewSet):
    queryset = Datos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DatosSerializer