# ejercicio9/Carrito.py
class Carrito:
    def __init__(self):
        self.productos = {}
        self.descuento = 0

    def agregar_producto(self, producto, cantidad):
        self.productos[producto] = self.productos.get(producto, 0) + max(0, int(cantidad))

    def calcular_total(self):
        total = sum(p.precio * q for p, q in self.productos.items())
        return total * (1 - self.descuento / 100)

    def aplicar_descuento(self, porcentaje):
        self.descuento = min(max(0, float(porcentaje)), 100)