#Crea una clase Mesa con número, capacidad y estado (ocupada o libre). Crea una clase Restaurante que permita agregar mesas, reservar, liberar y mostrar estado de todas las mesas
class Mesa:
    def __init__(self, numero, capacidad, estado):
        self.numero = numero
        self.capacidad = capacidad
        self.estado = estado
        estado = True

class Restaurante:
    def __init__(self):
        self.mesas = {}

    def agregar(self, mesa: Mesa):
        self.mesas[mesa.numero] = mesa
        print (f"Has agregado la mesa número: {mesa.numero} con capacidad para {mesa.capacidad} personas")

    def reservar(self, numero):
        if numero in self.mesas:
            if self.mesas[numero].estado == True:
                print (f"Has reservado la mesa número: {numero}")
            else:
                print (f"La mesa número: {numero} ya está ocupada")
            self.mesas[numero].estado = False
        else:
            print (f"La mesa número: {numero} no existe en el restaurante")

