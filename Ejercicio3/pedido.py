class Pedido:
    def __init__(self, nombre):
        self.nombre = nombre
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)
        print(f"\n* Se ha agregado {item.nombre} al pedido *")
    
    def calcular_total(self):
        if self.items:
            total = 0
            
            print(f"\n--- Detalle del pedido ---")
            for item in self.items:
                total += item.subtotal()
                print(f"* {item.nombre} ${item.precio} x {item.cantidad}")
            print(f"\nTotal: ${total}")
        else:
            print("\n--- El pedido está vacio ---")