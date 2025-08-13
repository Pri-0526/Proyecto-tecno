class Persona:
    def hablar (self):
        pass
class Padre (Persona):
    apellido= " "
    def __init__(self,nombre):
        self.nombre=nombre
    def __str__(self):
        return self.nombre + " " +self.apellido
    def hablar (self):
        print ("hola soy", self.nombre, self.apellido)

class Hijo (Padre): 
    def __init__(self,nombre,losDeportes):
        super().__init__(nombre)
        self.losDeportes=losDeportes
    def hablar (self):
        print ("hola soy",self.nombre,self.apellido, "y me gusta", self.losDeportes)
    
class Hija (Padre): 
    def __init__(self,nombre,Musica):
        super().__init__(nombre)
        self.Musica=Musica
    def hablar (self):
        print ("hola soy",self.nombre,self.apellido, "y me gusta", self.Musica)


padre = Padre("nombre del padre")
Padre.apellido= "apellido del padre"
hijo = Hijo ("nombre del hijo" , "python")
hijo.hablar ()
hija = Hija("nombre del hija" , "nombre de banda")
hija.hablar ()

#Crea una clase `Empleado` con atributos `nombre` y `salario`. Luego, define una subclase `Gerente` que herede de `Empleado` y añada un atributo `departamento`. Implementa un método `mostrar_informacion()` en ambas clases.