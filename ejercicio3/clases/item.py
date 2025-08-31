class Item:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = int(precio)
        self.cantidad = int(cantidad)
    
    def subtotal(self):
        
        subtotal = self.precio * self.cantidad
        return subtotal
    
    