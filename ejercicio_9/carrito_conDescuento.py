##Crea una clase Producto con nombre y precio. 
##Crea una clase Carrito que permita agregar productos con cantidad, calcular total y aplicar un descuento en porcentaje.

class Producto:
    def __init__(self, precio,nombre):
        self.precio = precio
        self.nombre = nombre

class Carrito:
    def __init__(self):
        self.items = []  

    def agregar_producto(self, producto, cantidad):
        self.items.append((producto, cantidad))

    def calcular_total(self):
        total = 0
        for producto, cantidad in self.items:
            total += producto.precio * cantidad
        return total

    def aplicar_descuento(self, porcentaje):
        total = self.calcular_total()
        descuento = total * (porcentaje / 100)
        return total - descuento

