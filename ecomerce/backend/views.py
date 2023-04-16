from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from backend.models import Usuario, Category, Article
from backend.serializers import UserSerializers, UserListSerializer, CategorySerializers, ArticleSerializers


@api_view(['GET'])
def prueba_api_view(request):
    listado = 'Bienvenido a Django Rest Framework'
    
    return  HttpResponse(listado)

@api_view(['GET', 'POST'])
def user_api_view(request):
    
    if request.method == 'GET':
       user = Usuario.objects.all().values('id', 'username', 'email', 'password')
       users_serializer = UserListSerializer(user, many=True)
       
       if users_serializer:
           print('paso las validaciones')
           
       return Response(users_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        users_serializer = UserSerializers(data = request.data)
        
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(users_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, pk=None):
    user = Usuario.objects.filter(id = pk).first()

    #Validacion
    if user: 
        
        if request.method == 'GET':
            user_serializers = UserSerializers(user)
            return Response(user_serializers.data, status = status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            user_serializer = UserSerializers(user, data = request.data)
            
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_200_OK)
            
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message': 'Usuario Eliminado Correctamente!'}, status = status.HTTP_200_OK)

    return Response({'message': 'Usuario Eliminado Correctamente!'}, status = status.HTTP_400_BAD_REQUEST)


#Metodos de las categorias

@api_view(['GET', 'POST'])
def categorias_view(request):
    if request.method == 'GET':
        categoria = Category.objects.all()
        category_serializer = CategorySerializers(categoria, many=True)
        return Response(category_serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
        category_serializer = CategorySerializers(data = request.data)
        
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(category_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def categoria_view(request, pk=None):
    category = Category.objects.filter(id = pk).first()

    #Validacion
    if category: 
        
        if request.method == 'GET':
            category_serializer = CategorySerializers(category)
            return Response(category_serializer.data, status = status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            category_serializer = UserSerializers(category, data = request.data)
            
            if category_serializer.is_valid():
                category_serializer.save()
                return Response(category_serializer.data, status = status.HTTP_200_OK)
            
            return Response(category_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            category.delete()
            return Response({'message': 'categoria Eliminada Correctamente!'}, status = status.HTTP_200_OK)

    return Response({'message': 'Error categoria no fue eliminada'}, status = status.HTTP_400_BAD_REQUEST)


#Metodos para los articluos

@api_view(['GET', 'POST'])
def articulos_view(request):
    if request.method == 'GET':
        articulos = Article.objects.all()
        articulos_serializer = CategorySerializers(articulos, many=True)
        return Response(articulos_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        articulos_serializer = ArticleSerializers(data = request.data)
        
        if articulos_serializer.is_valid():
            articulos_serializer.save()
            return Response(articulos_serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(articulos_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def articulo_view(request, pk=None):
    articulo = Article.objects.filter(id = pk).first()

    #Validacion
    if articulo: 
        
        if request.method == 'GET':
            articulo_serializer = CategorySerializers(articulo)
            return Response(articulo_serializer.data, status = status.HTTP_200_OK)
        
        elif request.method == 'PUT':
           articulo_serializer = UserSerializers(articulo, data = request.data)
            
        elif request.method == 'PUT':
            articulo_serializer = UserSerializers(articulo, data = request.data)
            
            if articulo_serializer.is_valid():
                articulo_serializer.save()
                return Response(articulo_serializer.data, status = status.HTTP_200_OK)
            
            return Response(articulo_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            articulo.delete()
            return Response({'message': 'categoria Eliminada Correctamente!'}, status = status.HTTP_200_OK)

    return Response({'message': 'Error categoria no fue eliminada'}, status = status.HTTP_400_BAD_REQUEST)