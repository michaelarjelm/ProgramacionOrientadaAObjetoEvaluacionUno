# ejercicio3/Item.py
class Item:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = max(0, float(precio))
        self.cantidad = max(1, int(cantidad))

    def subtotal(self):
        return self.precio * self.cantidad