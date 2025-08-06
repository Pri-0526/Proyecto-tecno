class Clase:
    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        return "El atributo es:" + self.atributo

    def imprimir(self):
        print("Imprimiendo: " + self.atributo)

instancia = Clase ("valor")
print(instancia.metodo())
instancia.imprimir()
#crear una clase que sume dos numeros y los muestre en pantalla

class Suma:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def calcular_suma(self):
        return self.numero1 + self.numero2

    def mostrar_resultado(self):
        print("El resultado de la suma es:", self.calcular_suma())

instancia = Suma(10, 5)
instancia.mostrar_resultado()
