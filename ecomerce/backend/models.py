from django.db import models
from usuarios.models import Usuario
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=255, verbose_name='Descripcion')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.descripcion
    
class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField( verbose_name='Imagen', upload_to='articles')
    public = models.BooleanField(verbose_name='Publicado?')
    usuario = models.ForeignKey(Usuario, verbose_name='Usuario', editable=False, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorias', blank=True, related_name="articles")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado el')
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.descripcion