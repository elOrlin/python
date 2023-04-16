from rest_framework import generics
from base.api import GeneralListApiView
from rest_framework import viewsets
from usuarios.autentication_mixin import Authentication
from productos.api.serializers.producto_serializers import ProductoSerializer
from rest_framework import status
from rest_framework.response import Response

class ProductoViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def list(self, request):
        print(self.user)
        producto_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(producto_serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado correctamente'}, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            producto_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            
            if producto_serializer.is_valid():
                producto_serializer.save()
                return Response(producto_serializer.data, status = status.HTTP_200_OK)
            return Response(producto_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        producto = self.get_queryset().filter(id = pk).first()
        if producto:
            producto.state = False
            producto.save()
            return Response({'message': 'Producto eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un producto con estos datos'})
    
    
    
    
    
    

'''
class ProductoListAPIView(GeneralListApiView):
    serializer_class = ProductoSerializer
    
class ProductoCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductoSerializer
    
class ProductoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductoSerializer
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, pk=None):
        if self.get_queryset(pk):
            producto_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            
            if producto_serializer.is_valid():
                producto_serializer.save()
                return Response(producto_serializer.data, status = status.HTTP_200_OK)
            return Response(producto_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        producto = self.get_queryset()
        if producto:
            producto_serializer = self.serializer_class(producto)
            return Response(producto_serializer.data, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un producto con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        if self.get_queryset(pk):
            producto_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            
            if producto_serializer.is_valid():
                producto_serializer.save()
                return Response(producto_serializer.data, status = status.HTTP_200_OK)
            return Response(producto_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
    def patch(self, request, pk=None):
        producto = self.get_queryset()
        if producto:
            producto_serializer = self.serializer_class(producto)
            return Response(producto_serializer.data, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un producto con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        producto = self.get_queryset().filter(id = pk).first()
        if producto:
            producto.state = False
            producto.save()
            return Response({'message': 'Producto eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un producto con estos datos'})
     
class ProductoDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
   

class ProductoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductoSerializer
    
    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id = pk).first()
    
    def patch(self, request, pk=None):
        producto = self.get_queryset()
        if producto:
            producto_serializer = self.serializer_class(producto)
            return Response(producto_serializer.data, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un producto con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        if self.get_queryset(pk):
            producto_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)'''