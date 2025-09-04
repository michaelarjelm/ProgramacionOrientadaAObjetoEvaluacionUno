class Item:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio} x Cantidad: {self.cantidad} = Subtotal: ${self.subtotal()}"
