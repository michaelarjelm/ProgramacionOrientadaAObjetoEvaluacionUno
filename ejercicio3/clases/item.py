# clases/Item.py
class Item:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self) -> float:
        return self.precio * self.cantidad

    def __str__(self) -> str:
        return f"{self.nombre} x {self.cantidad} = ${self.subtotal():.2f}"
