from item import Item

class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, nombre, precio, cantidad):
        nuevo_item = Item(nombre, precio, cantidad)
        self.items.append(nuevo_item)
        print(f"Item '{nombre}' agregado: {cantidad} unidad(es) a ${precio:.2f} cada una.")

    def calcular_total(self):
        total = sum(item.subtotal() for item in self.items)
        return total

    def mostrar_pedido(self):
        if not self.items:
            print("El pedido está vacío.")
            return
        print("Detalle del pedido:")
        for item in self.items:
            print(item)
        print(f"Total a pagar: ${self.calcular_total():.2f}")
