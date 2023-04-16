from productos.models import Producto
from rest_framework import serializers
from productos.api.serializers.general_serialisers import MeasureUnitSerializer, CategoriaProductoSerializer


class ProductoSerializer(serializers.ModelSerializer):
    #Cuando no haya que validar campos esta opcion es la correcta
   # mesure_unit = serializers.StringRelatedField()
    #categoria_producto = serializers.StringRelatedField()
    
    class Meta:
        model = Producto
        exclude = ('state', 'created_date', 'delete_date')
        
    #Si hay que validar campos esta forma es la correcta
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'descripcion': instance.descripcion,
            'image': str(instance.image if instance.image != '' else ''),
            'measure_unit': instance.measure_unit.descripcion if instance.measure_unit is not None else '',
            'categoria_producto': instance.categoria_producto.descripcion if instance.categoria_producto is not None else ''
        }