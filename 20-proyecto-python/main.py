from usuarios import acciones

print("""
Acciones disponibles:
    - Registro
    - Login
""")

info = acciones.Acciones()
accion = input('Que quieres hacer?: ')

if accion == 'Registro':
   info.registro()
   
elif accion == "Login":
    info.login()