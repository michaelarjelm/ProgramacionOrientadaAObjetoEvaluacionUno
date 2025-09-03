#Ejercicio 8 — Restaurante, Mesa y Reserva
#Crea una clase Mesa con número, capacidad y estado (ocupada o libre).
#Crea una clase Restaurante que permita agregar mesas, reservar, liberar y mostrar estado de todas las mesas.

class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False

class Restaurante:
    def __init__(self):
        self.mesas = []

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)

    def reservar_mesa(self, numero):
        mesa = self.buscar_mesa(numero)
        if mesa and not mesa.ocupada:
            mesa.ocupada = True
            return True
        return False

    def liberar_mesa(self, numero):
        mesa = self.buscar_mesa(numero)
        if mesa and mesa.ocupada:
            mesa.ocupada = False
            return True
        return False

    def mostrar_estado_mesas(self):
        for mesa in self.mesas:
            estado = "Ocupada" if mesa.ocupada else "Libre"
            print(f"Mesa {mesa.numero}: {estado}")

    def buscar_mesa(self, numero):
        for mesa in self.mesas:
            if mesa.numero == numero:
                return mesa
        return None
