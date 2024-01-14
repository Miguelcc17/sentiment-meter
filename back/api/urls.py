from rest_framework import routers
from .api import UserViewSet, DataViewSet

router = routers.DefaultRouter()

router.register('api/user', UserViewSet, 'user')
router.register('api/data', DataViewSet, 'data')

urlpatterns = router.urls
