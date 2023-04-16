from productos.models import MeasureUnit, CategoriaProducto, Indicador
from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = MeasureUnit
        exclude = ('state', 'created_date', 'delete_date')
        
class CategoriaProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CategoriaProducto
        exclude = ('state',)
        
class IndicadorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Indicador
        exclude = ('state',)