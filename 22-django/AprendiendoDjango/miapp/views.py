from django.shortcuts import render, HttpResponse, redirect

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
    
    html = """
        <ul>
    """
    year = 2023
    
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}"
        year += 1
    html += "<ul>"
    
    return render(request, 'index.html')

def nombreApellidos(request):
    nombre = "Orlin de los santos"
    apellidos = "Diaz Diaz"
    
    nombre_completo = f"{nombre} {apellidos}"
    
    return HttpResponse(layout+nombre_completo)


def prueba(request):
    return render(request, 'prueba.html')

def contacto(request, nombre="", apellidos="", edad=""):
    html = ""
    
    if nombre and apellidos and edad:
        html = "El nombre completo es:"
        html = f"{nombre} {apellidos} {edad}"
        
    return HttpResponse(layout+f"<h2>Contacto {nombre} {apellidos} {edad}</h2>"+html)