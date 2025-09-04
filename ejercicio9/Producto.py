# ejercicio9/Producto.py
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = max(0, float(precio))