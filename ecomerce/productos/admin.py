from django.contrib import admin
from productos.models import *

# Register your models here.
class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    
class CategoriaProductoAdmin(admin.ModelAdmin):
    read_only_fields = ('id', 'descripcion')
    
admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(Indicador)
admin.site.register(Producto)