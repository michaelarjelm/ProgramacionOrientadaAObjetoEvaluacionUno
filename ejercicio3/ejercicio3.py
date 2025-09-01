class Item:
    def __init__(self,precio,cantidad):
        self.precio = precio
        self.cantidad = cantidad
        subtotal = self.precio * self.cantidad
        print(subtotal)