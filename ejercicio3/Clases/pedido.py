from ejercicio3.Clases.item import Item

class Pedido:
    def __init__(self):
        self.items = []
    
    def agregar_item(self, item: Item):
        self.items.append(item)
        print(f"{item} ha sido agregado al pedido.")
    
    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item.subtotal()  
        return total
    
    def mostrar_pedido(self):
        if not self.items:
            print("El pedido está vacío.")
        else:
            print("\nPedido:")
            for item in self.items:
                print(f"{item.nombre} x{item.cantidad} - ${item.precio}, Subtotal: ${item.subtotal()}")
            print(f"\nTotal: ${self.calcular_total()}")