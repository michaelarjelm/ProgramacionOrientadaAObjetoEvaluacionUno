class Producto:
    def __init__(self,nombre,precio,cantidad,descuento):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descuento = descuento
        total = self.precio * self.cantidad
        total_descuento = total - (total*(self.descuento/100))
        print(f"el precio de su pedido es ${total} y al aplicar el {self.descuento}% de descuento, su pedido queda en ${total_descuento}")

