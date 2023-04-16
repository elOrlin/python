from rest_framework import serializers
from backend.models import Usuario, Category

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password']
        
    def create(self, validated_data):
        user = Usuario(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'nombre_usuario': instance['username'],
            'correo_electronico': instance['email'],
            'password': instance['password']
        }
        
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering = ['-created_at',]
        
    def __str__(self):
        return self.name
    
class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        verbose_name='Articulo'
        verbose_name_plural='Articulos'
        fields = '__all__'
        
    def __str__(self):
        return self.title