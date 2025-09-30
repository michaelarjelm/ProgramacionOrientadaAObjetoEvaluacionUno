class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)
        print(f"Ítem agregado: {item.nombre}")

    def calcular_total(self):
        total = sum(item.subtotal() for item in self.items)
        return total

    def mostrar_pedido(self):
        print("Pedido:")
        for item in self.items:
            print(f"{item.nombre},Precio: {item.precio} x {item.cantidad} = {item.subtotal()}")
        print(f"Total del pedido: {self.calcular_total()}")