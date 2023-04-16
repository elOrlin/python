from rest_framework.routers import DefaultRouter
from productos.api.views.productos_viewset import ProductoViewSet
from productos.api.views.general_views import *

router = DefaultRouter()

router.register(r'productos', ProductoViewSet, basename='productos')
router.register(r'measure_unit', MeasureUnitViewSet, basename='measure_unit')
router.register(r'indicador', IndicadorViewSet, basename='indicador')
router.register(r'categoria_producto', CategoriaProductoViewSet, basename='categoria_producto')

urlpatterns = router.urls
