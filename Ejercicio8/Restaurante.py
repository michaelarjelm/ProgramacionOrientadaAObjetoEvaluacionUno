from Ejercicio8.Mesa import Mesa

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mesas = []

    def agregar_mesa(self, numero, capacidad):
        # Evitar mesas duplicadas por número
        for m in self.mesas:
            if m.numero == numero:
                return False
        self.mesas.append(Mesa(numero, capacidad))
        return True

    def reservar_mesa(self, numero):
        for m in self.mesas:
            if m.numero == numero:
                return m.reservar()
        return False

    def liberar_mesa(self, numero):
        for m in self.mesas:
            if m.numero == numero:
                return m.liberar()
        return False
    
    def mostrar_estado(self):
        return [str(m) for m in self.mesas]