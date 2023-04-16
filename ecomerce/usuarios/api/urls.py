from rest_framework.routers import DefaultRouter

from usuarios.api import UserViewSet

router = DefaultRouter()

router.register('usuarios', UserViewSet, basename="usuarios")

urlpatterns = router.urls