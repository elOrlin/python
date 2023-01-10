import clases

persona = clases.Persona()
persona.setNombre('Orlin De Los Santos')
persona.setApellidos('Diaz Diaz')
persona.setEdad('24')
persona.setAltura('180cm')

print('------------------------------------------------------------')
print(f'La persona que programa javascript y python es: {persona.getNombre()} {persona.getApellidos()}')
print('------------------------------------------------------------')
informatico = clases.Informatico()
informatico.setNombre('Orielsy')
informatico.setApellidos('Diaz Espinal')

print(f'el informatico es: {informatico.getNombre()} {informatico.getApellidos()}')
print(f'{informatico.getLenguajes()}')
print(f'{informatico.programar()}')
print('------------------------------------------------------------')

tecnico = clases.TecnicoRedes()
tecnico.setNombre('Olvin Diaz')
print(f'el tecnico esta prendiendo en {tecnico.programar()} {tecnico.getNombre()}')