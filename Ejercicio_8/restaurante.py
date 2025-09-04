# Ejercicio 8 — Restaurante, Mesa y Reserva 
# Crea una clase Mesa con número, capacidad y estado (ocupada o libre). Crea una clase 
# Restaurante que permita agregar mesas, reservar, liberar y mostrar estado de todas las mesas. 

from mesa import Mesa

class Restaurante:
    def __init__(self):
        self.mesas = []

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)
        print(f" Mesa {mesa.numero} agregada al restaurante.")

    def reservar_mesa(self, numero):
        for mesa in self.mesas:
            if mesa.numero == numero:
                mesa.reservar()
                return
        print(f" No se encontró la mesa {numero}.")

    def liberar_mesa(self, numero):
        for mesa in self.mesas:
            if mesa.numero == numero:
                mesa.liberar()
                return
        print(f" No se encontró la mesa {numero}.")

    def mostrar_estado_mesas(self):
        if not self.mesas:
            print(" No hay mesas en el restaurante.")
        else:
            print("\n--- Estado de las Mesas ---")
            for mesa in self.mesas:
                print(mesa)

