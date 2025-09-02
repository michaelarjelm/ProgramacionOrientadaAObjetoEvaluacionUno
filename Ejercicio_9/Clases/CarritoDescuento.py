# Crea una clase Producto con nombre y precio. Crea una clase Carrito que permita agregar productos con cantidad, calcular total y aplicar un descuento en porcentaje.
import math
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.listaCarrito = {}

    def agregar (self, producto: Producto, cantidad):
        if cantidad > 0:
            if producto in self.listaCarrito:
                self.listaCarrito[producto] += cantidad
            else:
                self.listaCarrito[producto] = cantidad
                print(f"Se agregaron {cantidad} de '{producto.nombre}' al carrito.")

    def calcularTotal (self):
            total = 0
            for producto, cantidad in self.listaCarrito.items(): 
                total += producto.precio * cantidad
            return total
    
    def descuento(self, porcentaje: float):
        total = self.calcularTotal()
        if 0 <= porcentaje <= 100:
            totalFinal = total * (1 - porcentaje / 100)
            print(f"El total con descuento aplicado es: ${totalFinal}")
            return totalFinal
        else:
            print("Porcentaje de descuento inválido.")
            return total