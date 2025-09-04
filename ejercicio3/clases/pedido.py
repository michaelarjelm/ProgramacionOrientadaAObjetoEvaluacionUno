# Crea una clase Pedido que permita agregar ítems y calcular el total.
from .item import Item

class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, item: Item, precio: float = None, cantidad: int = None):
        self.items.append(item)
        print(f'Se ha agregado:{item} al pedido.')

    def calcular_total(self) -> float:
        total = sum(item.subtotal() for item in self.items)
        print(f'El total del pedido es: {total}')
        return total        

    def listar_items(self):
        for item in self.items:
            print(item)
        return  self.items



       