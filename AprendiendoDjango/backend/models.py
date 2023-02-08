from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default="null")
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Articulo',
        verbose_name_plural = 'Articulos'
        ordering = ['public']
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    create_at = models.DateField()
    
    class Meta:
        verbose_name = 'Categoria',
        verbose_name_plural = 'Categorias'