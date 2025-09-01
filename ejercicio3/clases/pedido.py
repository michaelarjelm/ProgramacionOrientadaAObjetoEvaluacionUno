class Pedido:
    def __init__(self):
        self.items = []
    
    def agregar_item(self,item):
        self.items.append(item)
        print(f"Se ha agregado {item.nombre} al pedido")


    def detalle_pedido(self):
        print("Detalle del pedido: ")
        for item in self.items:
            print(f"{item.nombre} - Precio: ${item.precio} - Cantidad: {item.cantidad} - Subtotal: ${item.subtotal()}")
        

    def calculo_total(self):
        
        total = 0
        for item in self.items:
            total += item.subtotal()
        return total
