class Carrito:
    def __init__(self):
        self.productos = []

    
    
    def agregar_producto(self,producto):
        self.productos.append(producto)
        print("Producto agregado al carrito")

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio * producto.cantidad
        return total
    


    def descuento(self, porcentaje):
        total = self.calcular_total()
        total_con_descuento = total - (total * porcentaje / 100)
        return round(total_con_descuento)
                                
