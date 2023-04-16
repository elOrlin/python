from django.contrib import admin
from .models import Category, Article
from usuarios.models import Usuario

# Register your models here.
admin.site.register(Category)
admin.site.register(Article)