#creamos el from import 
from ejercicio8.clases.Mesa import Mesa
# creamos la clase restaurante, con numero de mesa y con la capacidad 
class Restaurante:
    def __init__(self):
        self.mesas = []
# definimos agregar mesa tipo reserva 
    def agregar_mesa(self, numero, capacidad):
        self.mesas.append(Mesa(numero, capacidad))
# definimos reservar mesa como tal 
    def reservar(self, numero):
        for m in self.mesas:
            if m.numero == numero:
                return m.reservar()
        return False
# definimos liberar mesa 
    def liberar(self, numero):
        for m in self.mesas:
            if m.numero == numero:
                return m.liberar()
        return False
# esto no mostrara las mesa que estan ocupadas 
    def mostrar(self):
        for m in self.mesas:
            print(m)
