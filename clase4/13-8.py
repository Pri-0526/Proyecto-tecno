class Persona:
    def hablar(self):
        pass
class Padre(Persona):
    apellido=''
    def __init__(self,nombre):
        self.nombre=nombre
    def __str__(self):
        return self.nombre+" "+self.apellido
    def hablar(self):
        print("hola soy",self.nombre,self.apellido)

class Hijo(Padre):
    def __init__(self,nombre,lenguajesDeProgramacion):
        super().__init__(nombre)
        self.lenguajesDeProgramacion=lenguajesDeProgramacion
    def hablar(self):
        print("hola soy",self.nombre,self.apellido,"y me gusta",self.lenguajesDeProgramacion)

class Hija(Padre):
    def __init__(self,nombre,artistaMusical):
        super().__init__(nombre)
        self.artistaMusical=artistaMusical
    def hablar(self):
        print("hola soy",self.nombre,self.apellido,"y me gusta",self.artistaMusical)

padre = Padre('nombre del padre')
Padre.apellido='apellido del padre'
hijo = Hijo('nombre del hijo','python')
hijo.hablar()
hija = Hija('nombre del hija','nombre de banda')
hija.hablar() 

#Crea una clase `Empleado` con atributos `nombre` y `salario`. Luego, define una subclase `Gerente` que herede de `Empleado` y añada un atributo `departamento`. Implementa un método `mostrar_informacion()` en ambas clases.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_informacion(self):
        print(f"Empleado: {self.nombre}, Salario: ${self.salario}")

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)  # Llamamos al constructor de Empleado
        self.departamento = departamento

    def mostrar_informacion(self):
        print(f"Gerente: {self.nombre}, Salario: ${self.salario}, Departamento: {self.departamento}")

empleado1 = Empleado("Ana López", 50000)
gerente1 = Gerente("Carlos Pérez", 80000, "Recursos Humanos")

empleado1.mostrar_informacion()
gerente1.mostrar_informacion()
