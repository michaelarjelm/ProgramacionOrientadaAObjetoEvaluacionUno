# Creamos el producto

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.articulos = []
        
    def agregar_producto(self, producto, cantidad):
        self.articulos.append({'producto': producto, 'cantidad': cantidad})
        print(f"Añadiste '{cantidad}' de '{producto.nombre}' al carrito. ")
    
    def calcular_total(self):
        total = 0
        for articulo in self.articulos:
            total += articulo['producto'].precio * articulo['cantidad']
        return total
    
    def aplicar_descuento(self, porcentaje):
        total_sin_descuento = self.calcular_total()
        descuento = total_sin_descuento * (porcentaje / 100)
        total_a_apagar = total_sin_descuento - descuento
        return total_a_apagar