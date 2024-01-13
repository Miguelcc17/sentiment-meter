from rest_framework import routers
from .api import UsuariosViewSet, DatosViewSet

router = routers.DefaultRouter()

router.register('api/user', UsuariosViewSet, 'user')
router.register('api/datos', DatosViewSet, 'datos')

urlpatterns = router.urls
