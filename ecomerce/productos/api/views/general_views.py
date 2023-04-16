from rest_framework import viewsets
from rest_framework.response import Response
from base.api import GeneralListApiView
from productos.models import MeasureUnit
from productos.api.serializers.general_serialisers import MeasureUnitSerializer, IndicadorSerializer, CategoriaProductoSerializer


class MeasureUnitViewSet(viewsets.GenericViewSet):
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)
    
    
class IndicadorViewSet(viewsets.ViewSet):
    serializer_class = IndicadorSerializer
    
class CategoriaProductoViewSet(viewsets.ViewSet):
    serializer_class = CategoriaProductoSerializer