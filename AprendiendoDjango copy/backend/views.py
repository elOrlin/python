from django.shortcuts import render, HttpResponse, redirect
from backend.models import Article
from django.db.models import Q
from backend.forms import FormArticle
from django.contrib import messages

# Create your views here.
layout = """ 
        <h1>Sitio web con django | Orlin Diaz Diaz</h1>
        <hr/>
        <nav>
            <ul>
                <li><a href="/hola-mundo"</a>Orlin Diaz Diaz</li>
                <li><a href="/inicio" </a>Otniel Diaz Diaz</li>
                <li><a href="/nombreApellido" </a>Olvin Diaz Diaz</li>
                <li><a href="/hola-mundo" </a>telefono</li>
            </ul>
        </nav>
        <hr/>
    """

def inicio(request):
    return HttpResponse(layout)
    

def holamundo(request):
    return render(request, 'holamundo.html')

def pagina(request, redirigir=0):
    
    if redirigir == 1: 
        return redirect('/nombreApellido/', nombre="Orlin", apellidos="Diaz")
    
    return HttpResponse(layout+"cargando paginas de las vistas")



def inicioyear(request):
    '''
    html = """
        <ul>
    """
    year = 2023
    
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}"
        year += 1
    html += "<ul>" '''
    
    year = 2023
    hasta = range(year, 2051)
    
    return render(request, 'index.html', {
        'years': hasta
    })

def nombreApellidos(request):
    nombre = "Orlin de los santos"
    apellidos = "Diaz Diaz"
    
    nombre_completo = f"{nombre} {apellidos}"
    
    lenguajes = ['Javascirpt', 'Reac.js', 'Node.js', 'Python', 'Tkinter', 'Django']
    
    return render(request, 'index.html', {
        "mi_variable": "Soy una vista mostrada en la template de django",
        "nombre": nombre_completo,
        "lenguajes": lenguajes
    })


def prueba(request):
    return render(request, 'pagina.html', {
        'texto': "",
        "lista": ['uno', 'dos', 'tres']
    })

def contacto(request, nombre="", apellidos="", edad=""):
    html = ""
    
    if nombre and apellidos and edad:
        html = "El nombre completo es:"
        html = f"{nombre} {apellidos} {edad}"
        
    return HttpResponse(layout+f"<h2>Contacto {nombre} {apellidos} {edad}</h2>"+html)

#creando los articulos y guardando en la base de datos
def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )
    
    articulo.save()
    
    return HttpResponse(f'Articulo Creado: {articulo.title} {articulo.content} {articulo.public}')

def save_articulo(request):
    if request.method == "POST":
        
        title = request.POST['title']
        
        if len(title) <= 5:
             return HttpResponse(f'El titulo es muy pequeno')
        
        content = request.POST['content']
        public = request.POST['public']
        
        articulo = Article(
            title = title,
            content = content,
            public = public
        )
    
        articulo.save()
        return HttpResponse(f'Articulo guardado: {articulo.title} {articulo.content} {articulo.public}')
    
    else:
        return HttpResponse(f'<h2>No se ha podido crear el articulo...</h2>')
    
def create_article(request):
    
    return render(request, 'create-article.html')

#(mostrar/obtener) los articulos
def articulo(request):
    
    try:
        articulo = Article.objects.get(pk=9, public=False)
        response = f'<h1>Articulo: {articulo.id}. {articulo.title} {articulo.content}</h1>'
    except:
        response = "<h1>Articulo no encontrado</h1>"
        
    return HttpResponse(response)

#editar los articulos
def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    
    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True
    
    articulo.save()
    
    return HttpResponse(f'Articulo Editado: {articulo.title} {articulo.content} {articulo.public}')

def create_full_article(request):
    
    if request.method == 'POST':
        formulario = FormArticle(request.POST)
        
        if formulario.is_valid():
            form_data = formulario.cleaned_data
            
            title = form_data.get('title')
            content = form_data['content']
            public = form_data['public']
            
            articulo = Article(
                title = title,
                content = content,
                public = public
            )
            
            articulo.save()
            
            #crear mensajes flash que solo se muestra una vez
            messages.success(request, f'Has creado correctamente el articulo {articulo.id}')
            
            return redirect('articulos')
    else:
        formulario = FormArticle()
    
    return render(request, 'create_full_article.html', {
        'form': formulario
    })

def articulos(request):
    articulos = Article.objects.all().order_by("-id")
    
    #articulos = Article.objects.filter(title__contains="Javascritpt and Python")
    #articulos = Article.objects.filter(title__exact="Javascritpt and Python")
    
    #mayor a la cantidad 
    #articulos = Article.objects.filter(id__gt=17)
    
    ##mayor o igual
    #articulos = Article.objects.filter(id__gte=13)
    
    #menores a la cantidad
   # articulos = Article.objects.filter(id__lt=13)
    
    #menor o igual
    #articulos = Article.objects.filter(id__lte=13, title__contains="Progrmacion con python")
    '''
    articulos = Article.objects.filter(
        Q(title__contains="11") | Q(public=False)
    )
    
   articulos = Article.objects.filter(id__gte=10).exclude(public=True)
   
   articulos = Article.objects.raw("SELECT * FROM backend_article WHERE title='Articulo 2' AND public=0")
    '''
    return render(request, 'articulos.html', {
        'articulos': articulos
    })
    
def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    
    articulo.delete()
    return redirect('articulos')