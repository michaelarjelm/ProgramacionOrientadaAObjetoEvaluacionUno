#Crea una clase ítem con nombre, precio y cantidad, y un método subtotal().
class Item:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self) -> float:
        return self.precio * self.cantidad
    def __str__(self):
        return f'Item: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}, Subtotal: {self.subtotal()}'
    
    
    