
try:
    nombre = input('cual es tu nombre?:')
    
    if len(nombre) > 1:
        nombre_usuario = 'El nombre es ' + nombre
        
    print(nombre_usuario)
except:
    print('Ha ocurrido un error')
else:
    print('Todo a funcionado correctamente')
    
    #manejar multiples excepciones
    
    try:
        numero = int(input('Numero para elevarlo al cuadrado: '))
        print(f'cuadrado del numero {str(numero*numero)}')
        
    except TypeError:
        print('Debes convertir tus cadenas a enteros en el codigo')
        
    except ValueError:
        print('Debes poner un numero valido')
        
    except Exception as e:
        print(f'Ha ocurrido un error: {type(e).__name__}')
        
        
#excepciones personalizadas o lanzar excepcion
    
try:
    nombre = input('Introduce el nombre:')
    edad = int(input('Introduce la edad:'))
    
    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError('El nombre no esta completo')
    else:
        print(f'Bienvenido al master en python {nombre}')
except ValueError:
    print('Introudce los datos correctos')
except Exception as e:
    print('Existe un error:', e)