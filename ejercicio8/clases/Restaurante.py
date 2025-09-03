#creamos el from import 
from ejercicio8.clases.Mesa import Mesa
# creamos la clase restaurante, con numero de mesa y con la capacidad 
class Restaurante:
    def __init__(self):
        self.mesas = []

    def agregar_mesa(self, numero, capacidad):
        self.mesas.append(Mesa(numero, capacidad))

    def reservar(self, numero):
        for m in self.mesas:
            if m.numero == numero:
                return m.reservar()
        return False

    def liberar(self, numero):
        for m in self.mesas:
            if m.numero == numero:
                return m.liberar()
        return False

    def mostrar(self):
        for m in self.mesas:
            print(m)
