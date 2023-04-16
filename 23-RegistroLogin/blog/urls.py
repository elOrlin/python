from django.urls import path
from . import views

urlpatterns = [
     path('articulos/', views.lista, name='lista_articulos'),
     path('categoria/<int:category_id>', views.category, name='category'),
     path('articulo/<int:article_id>', views.article, name='article')
]
