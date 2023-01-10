#HERENCIA: es la posibilidad de compartir atributos y metodos, entre clases diferentes hereden de otras

class Persona():
    '''
    nombre
    apellidos
    edad
    altura
    '''
    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos
    
    def getEdad(self):
        return self.edad
    
    def getAltura(self):
        return self.altura
    
    def setNombre(self, nombre):
        self.nombre = nombre
        
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
        
    def setEdad(self, edad):
        self.edad = edad
        
    def setAltura(self, altura):
        self.altura = altura
        
    def caminar(self):
        return 'estoy caminando'
    
    def hablar(self):
        return 'estoy hablando'
    
    def dormir(self):
        return 'estoy durmiendo'
    
class Informatico(Persona):
    '''
    lenguajes
    experiencia
    '''
    def __init__(self):
        self.lenguajes = 'HTML5, CSS3, SASS, JAVASCRIPT, PYTHON'
        self.experiencia = 5
        
    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return 'Estoy programando'
    
    def repararPc(self):
        return 'He repado tu ordenador'
    
class TecnicoRedes(Informatico):
    
    def __init__(self):
        super().__init__()
        self.auditorRedes = 'Experto'
        self.experienciaRedes = 15
        
        def auditoria(self):
            return 'Estoy auditando una red'