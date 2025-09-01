# Ejercicio 8 — Restaurante, Mesa y Reserva
# Crea una clase Mesa con número, capacidad y estado (ocupada o libre). Crea una clase
# Restaurante que permita agregar mesas, reservar, liberar y mostrar estado de todas las mesas.

class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.estado = True

class Restaurante:
    def __init__(self,):
        pass