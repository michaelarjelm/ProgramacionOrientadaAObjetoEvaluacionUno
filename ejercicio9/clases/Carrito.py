# cmo es abitual primero hacemos el from para llamar al producto 
from ejercicio9.clases.Producto import Producto
# creamos la clase Carrito 
class Carrito:
    def __init__(self):
        self.items = []  # Esta es la lista de (producto, cantidad)

    def agregar(self, producto, cantidad):
        self.items.append((producto, cantidad))   # definomos agragar para agragar producto, y cantidad 

    def total(self):   # definimos el total para luego sacar el porcentaje de descuento que se le hara al total de la compra 
        return sum(p.precio * c for p, c in self.items)

    def total_con_descuento(self, porcentaje):    # definimos el descuento, y la operacion del porcentaje total * el porcentaje a descontar 
        return self.total() * (1 - porcentaje / 100)

    def mostrar(self):
        for p, c in self.items:
            print(f"{p.nombre} x{c} = ${p.precio * c}")
        print("El Total de la compra es:", self.total())
# definimos mostrar, esto nos dara el total final con descuento 