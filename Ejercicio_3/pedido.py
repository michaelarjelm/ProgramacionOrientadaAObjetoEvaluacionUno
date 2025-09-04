# Ejercicio 3 — Pedido e Ítem 
# Crea una clase ítem con nombre, precio y cantidad, y un método subtotal(). Crea una clase Pedido 
# que permita agregar ítems y calcular el total. 

from item import Item

class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)
        print(f" Se agregó el ítem: {item.nombre}")

    def calcular_total(self):
        total = sum(item.subtotal() for item in self.items)
        return total

    def mostrar_pedido(self):
        if not self.items:
            print(" El pedido está vacío.")
        else:
            print("\n--- Detalle del Pedido ---")
            for item in self.items:
                print(item)
            print(f" Total: ${self.calcular_total()}")
