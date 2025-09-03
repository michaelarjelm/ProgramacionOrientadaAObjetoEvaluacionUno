# clases/Pedido.py
from ejercicio3.clases.item import Item

class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, item: Item):
        self.items.append(item)

    def calcular_total(self) -> float:
        return sum(item.subtotal() for item in self.items)

    def mostrar_detalle(self):
        for item in self.items:
            print(item)
        print(f"El Total de tu Compra es:  = ${self.calcular_total():.2f}")
