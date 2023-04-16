from django.db import models

# Create your models here.
from simple_history.models import HistoricalRecords
from base.models import BaseModel
from usuarios.models import Usuario

# Create your models here.
class MeasureUnit(BaseModel):
    descripcion = models.CharField('Descripcion', max_length=50, blank= False, null = False, unique= True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _histroy_user(self, value):
        self.changed_by = value
        
    class Meta:
        verbose_name = ("Unidad de Medida")
        verbose_name_plural = ("Unidad de Medidas")

    def __str__(self):
        return self.descripcion

class CategoriaProducto(BaseModel):
    descripcion = models.CharField('Descripcion', max_length=50, blank= False, null = False, unique= True)
    historical = HistoricalRecords()
    
    class Meta:
        verbose_name="Categoria de Producto"
        verbose_name_plural="Categoria de Productos"
        
    def __str__(self):
        return self.descripcion

class Indicador(BaseModel):
    descuento = models.PositiveSmallIntegerField(default=0)
    categoria_producto = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE, verbose_name="Indicador de Oferta")
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Indicador de Ofertas'
        verbose_name_plural = 'Indicadores DE Ofertas'
        
    def __str__(self):
        return f'Oferta de la categoria {self.categoria_producto} : {self.descuento}%'
    
class Producto(BaseModel):
    name = models.CharField('Nombre de Producto', max_length=150, unique=True, blank= False, null = False)
    descripcion = models.TextField('Descripcion del producto', blank=True, null = False)
    image = models.ImageField('Imagen del Producto', upload_to='productos/', height_field=None, width_field=None, max_length=None, null = True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medidas', null = True)
    categoria_producto = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE, verbose_name='Categoria de Producto', null = True)
    usuario = models.ForeignKey(Usuario, verbose_name='Usuario', on_delete=models.CASCADE, null = True)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")
    
    def __str__(self):
        return self.name
        
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _histroy_user(self, value):
        self.changed_by = value