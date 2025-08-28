# Ejercicio 3 — Pedido e Ítem
# Crea una clase ítem con nombre, precio y cantidad, y un método subtotal(). Crea una clase Pedido
# que permita agregar ítems y calcular el total.

class Item:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def subtotal(self):
        return self.precio * self.cantidad
    
item = Item("caca", 500, 3)
subtotal = item.subtotal()
print(subtotal)

class Pedido:
    def __init__(self):
        items = []