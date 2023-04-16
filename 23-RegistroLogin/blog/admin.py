from django.contrib import admin
from .models import Category, Article

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at',)
    search_fields = ('name', 'descripcion')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'update_at')
    search_fields = ('title', 'content', 'user__username', 'categories__name')
    list_display = ('title', 'user', 'public', 'created_at')
    list_filter = ('public', 'user__username', 'categories__name')
    
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
            
        obj.save()

# Register your models here.
#estos metodos fueron cambiado por @admin.register
#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Article, ArticleAdmin)