from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from blog.models import Category, Article

# Create your views here.
def lista(request):
    #sacar los articulos
    articles = Article.objects.all()

    publico = Article.objects.filter(public=True)
    
    #Paginar los articulos
    paginator = Paginator(articles, 2)
    
    #recorrer numero de paginas
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    
    return render(request, 'articles/lista.html', {
        'title': 'Articulos',
        'articles': page_articles
    })
    
def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    #articles = Article.objects.filter(categories=category
    
    return render(request, 'categories/category.html', {
        'category': category,
        #'articles': articles
    })
    
    
def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    #articles = Article.objects.filter(Article=article_id)

    return render(request, 'articles/articulo.html', {
        'article': article
    })