# Ejercicio 9 — Carrito con Descuento 
# Crea una clase Producto con nombre y precio. Crea una clase Carrito que permita agregar 
# productos con cantidad, calcular total y aplicar un descuento en porcentaje. 

from producto import Producto

class Carrito:
    def __init__(self):
        self.items = []  

    def agregar_producto(self, producto, cantidad):
        self.items.append((producto, cantidad))
        print(f" {cantidad} unidad(es) de '{producto.nombre}' agregada(s) al carrito.")

    def calcular_total(self):
        total = sum(producto.precio * cantidad for producto, cantidad in self.items)
        return total

    def aplicar_descuento(self, porcentaje):
        total = self.calcular_total()
        descuento = total * (porcentaje / 100)
        total_con_descuento = total - descuento
        return total_con_descuento

    def mostrar_carrito(self):
        if not self.items:
            print(" El carrito está vacío.")
        else:
            print("\n--- Carrito de Compras ---")
            for producto, cantidad in self.items:
                subtotal = producto.precio * cantidad
                print(f"{producto.nombre} - Precio: ${producto.precio} x {cantidad} = Subtotal: ${subtotal}")
            print(f" Total: ${self.calcular_total()}")
