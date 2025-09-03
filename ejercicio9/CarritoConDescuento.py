#Ejercicio 9 — Carrito con Descuento
#Crea una clase Producto con nombre y precio.
#Crea una clase Carrito que permita agregar productos con cantidad, calcular total y aplicar un descuento en porcentaje.

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))

    def calcular_total(self):
        return sum(producto.precio * cantidad for producto, cantidad in self.productos)

    def aplicar_descuento(self, porcentaje):
        total = self.calcular_total()
        return total - (total * porcentaje / 100)
