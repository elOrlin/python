#crear diccionarios
"""
    Diccionario:
    Un tipo de datos que almacena un conjunto de datos.
    en formato clave > valor.
    es parecido a un array asociativo o un objecto json
"""

persona = {
    'nombre': 'orlin',
    'apellido': 'Diaz',
    'web': 'orlindiazweb.es'
}

print(persona['web'])

#diccionarios dentro de listas

contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antonio@antonio.com'
    },
    {
      'nombre': 'oliver',
       'email': 'oliverdiaz@outlook.com'
    },
    {
       'nombre': 'olvin',
       'email': 'olvindiaz@outlook.com'
    }
]

contactos[0]['nombre'] = 'Orlin'
contactos[0]['email'] = 'Orlindiaz@outlook.com'
print(contactos[0]['email'])

print("\nListado de contactos:")

print("------------------------------------------")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"email del contacto: {contacto['email']}")
    
print("------------------------------------------")