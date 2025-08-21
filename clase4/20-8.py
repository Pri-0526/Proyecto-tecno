import random

class Azar:
    def __init__(self,minimo,maximo):
        self.minimo=minimo
        self.maximo=maximo
        self.numero_al_azar=random.randint(self.minimo,self.maximo)
    def mostrar_numero(self):
        print(self.numero_al_azar)

instancia=Azar(1,255)
instancia.mostrar_numero()
