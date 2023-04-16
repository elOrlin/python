from blog.models import Category, Article

def get_categories(request):
    
    categorias_in_use = Article.objects.filter(public=True).values_list('categories', flat=True)
    categorias = Category.objects.filter(id__in=categorias_in_use).values_list('id', 'name')
    
    return {
        'categorias': categorias,
        'id': categorias_in_use
    }