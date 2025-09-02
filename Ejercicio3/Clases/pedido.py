#Clase pedido
class Pedido:
    def __init__(self, item):
        self.items = [item]
        
    def total(self):
        suma = 0
        for item in self.items:
            suma += item.subtotal()
        return suma