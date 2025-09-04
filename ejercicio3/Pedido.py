# ejercicio3/Pedido.py
class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def calcular_total(self):
        return sum(item.subtotal() for item in self.items)