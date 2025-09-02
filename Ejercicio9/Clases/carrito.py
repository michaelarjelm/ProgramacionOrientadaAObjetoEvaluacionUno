#Clase Carrito
class Carrito:
    def __init__(self):
        self.productos = []
        
    def agregar_productos(self, producto, cantidad):
        self.productos.append({"Producto": producto, "Cantidad": cantidad})
        
    def calcular_total(self):
        total = 0
        for item in self.productos:
            total += item ["producto"].precio * item["cantidad"]
        return total
    
    def aplica_descuento(self, porcentaje_descuento):
        total = self.calcular_total()
        descuento = total * (porcentaje_descuento / 100)
        return total - descuento