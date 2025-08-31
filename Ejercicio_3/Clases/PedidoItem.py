#Crea una clase ítem con nombre, precio y cantidad, y un método subtotal(). Crea una clase Pedido que permita agregar ítems y calcular el total.
class Item:
    def __init__ (self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def subtotal (self):
        return self.precio * self.cantidad
        

class Pedido:
    def __init__(self):
        self.listadoItems = []

    def agregar (self, item : Item):
        self.listadoItems.append (item)
        print(f"Has agregado {item.cantidad} del siguiente item: {item.nombre} a tu carrito, el valor es {item.subtotal()} ")
    
    def total (self):
        totalPedido = 0
        for item in self.listadoItems:
            totalPedido += item.subtotal()
        return totalPedido
