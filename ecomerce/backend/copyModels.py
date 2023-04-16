from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre', unique=True)
    descripcion = models.CharField(max_length=255, verbose_name='Descripcion')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    
    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        ordering = ['-id']
        
    def __str__(self):
        return self.name
    
class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name="nombre")
    
    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        ordering = ['-id']
        
    def __str__(self):
        return self.name

class Employee(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="nombre")
    dni = models.CharField(max_length=100, unique=True, verbose_name="Dni")
    apellidos = models.CharField(max_length=150, verbose_name="Apellidos")
    fecha = models.DateField(default=datetime.now, verbose_name="fecha registro")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado el')
    edad = models.PositiveIntegerField(default=0)
    salario = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    user = models.ForeignKey(User, verbose_name='Usuario', editable=False, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    sexo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    curriculum = models.FileField(upload_to='curriculum', null=True, blank=True)
    
    class Meta:
        verbose_name='Empleos'
        verbose_name_plural='Empleos'
        ordering = ['-id']
        
    def __str__(self):
        return self.name
    
class Producto(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='producto/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
        ordering = ['-id']
        
    def __str__(self):
        return self.name
    
class Cliente(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    apellidos = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    nacimiento = models.DateField(default=datetime.now, verbose_name='Fecha Nacimiento')
    direccion = models.CharField(max_length=150, null=True, blank=True, verbose_name='Direccion')
    sexo = models.CharField(max_length=10, default='male', verbose_name='Sexo')
    
    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
        ordering = ['-id']
        
    def __str__(self):
        return self.name
    
class Venta(models.Model):
    cli = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    class Meta:
        verbose_name='Venta'
        verbose_name_plural='Ventas'
        ordering = ['-id']
        
    def __str__(self):
        return self.cli
    
class DetSale(models.Model):
    sale = models.ForeignKey(Venta, on_delete=models.CASCADE)
    prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    class Meta:
        verbose_name='DetSale'
        verbose_name_plural='DetSales'
        ordering = ['-id']
        
    def __str__(self):
        return self.sale