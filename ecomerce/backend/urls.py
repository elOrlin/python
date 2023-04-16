from django.urls import path
#from . import views
from backend.views import prueba_api_view, user_api_view, user_detail_view, categorias_view, categoria_view, articulos_view, articulo_view

urlpatterns = [
    path('', prueba_api_view, name="pruebas"),
    path('usuario/', user_api_view, name='usuario_api'),
    path('usuario/<int:pk>/', user_detail_view, name="usuario_user_detail_view"),
    
    path('categorias/', categorias_view, name="categoria"),
    path('categoria/<int:pk>/', categoria_view, name="categoria_id"),
    
    path('articulos/', articulos_view, name='articulos'),
    path('articulos/<int:id>/', articulo_view, name='articulos_id')
]