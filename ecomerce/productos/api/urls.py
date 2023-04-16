from django.urls import path
from productos.api.views.general_views import MeasureUnitListAPIView, IndicadorlistAPIView, CategoriaProductoListAPIView
from productos.api.views.productos_viewset import ProductoListAPIView,  ProductoRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('indicador/', IndicadorlistAPIView.as_view(), name='indicador'),
    path('categoria_producto/', CategoriaProductoListAPIView.as_view(), name='categoria_producto'),
    path('producto/', ProductoListAPIView.as_view(), name='producto'),
    path('producto/retrieve-update-destroy/<int:pk>/', ProductoRetrieveUpdateDestroyAPIView.as_view(), name='producto_retrieve_update_destroy'),
    path('producto/destroy/<int:pk>/', ProductoRetrieveUpdateDestroyAPIView.as_view(), name='producto_destroy'),
    path('producto/update/<int:pk>/', ProductoRetrieveUpdateDestroyAPIView.as_view(), name='producto_update')
]






'''
from django.urls import path
from . import views
from backend.views import prueba_api_view, user_api_view, user_detail_view, categorias_view, categoria_view, articulos_view, articulo_view

urlpatterns = [
    path('', prueba_api_view, name="pruebas"),
    path('usuario/', user_api_view, name='usuario_api'),
    path('usuario/<int:pk>/', user_detail_view, name="usuario_user_detail_view"),
    
    path('categorias/', categorias_view, name="categoria"),
    path('categoria/<int:pk>/', categoria_view, name="categoria_id"),
    
    path('articulos/', articulos_view, name='articulos'),
    path('articulos/<int:id>/', articulo_view, name='articulos_id')''
]'''