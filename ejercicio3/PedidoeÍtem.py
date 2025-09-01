#Creacion de ítems

class Ítem:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def Subtotal(self):
        return self.precio * self.cantidad
    
#Creamos el pedido

class Pedido:
    def __init__(self):
        self.items = []
        
    def agregaritem(self, item):
        self.items.append(item)
        print(f'Has añadido "{item.cantidad}" al pedido de "{item.nombre}", con un monto de "{item.subtotal}".')
        
    def totalpedido(self):
        total <= 0
        for item in self.items:
            total += item.subtotal()
        return total