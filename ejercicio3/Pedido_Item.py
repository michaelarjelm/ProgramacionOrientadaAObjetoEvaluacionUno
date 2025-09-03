#Ejercicio 3 — Pedido e Ítem
#Crea una clase ítem con nombre, precio y cantidad, y un método subtotal().
#Crea una clase Pedido que permita agregar ítems y calcular el total.

class Item:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self):
        return self.precio * self.cantidad

class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def calcular_total(self):
        return sum(item.subtotal() for item in self.items)
