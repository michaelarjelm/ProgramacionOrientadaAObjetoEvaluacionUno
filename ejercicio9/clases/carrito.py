# Crea una clase Carrito que permita agregar 
# productos con cantidad, calcular total y aplicar un descuento en porcentaje..
class carrito:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad
        print(f"Agregado {cantidad} de {producto.nombre} al carrito.")

    def calcular_total(self):
        total = sum(producto.precio * cantidad for producto, cantidad in self.productos.items())
        return total

    def aplicar_descuento(self, porcentaje):
        total = self.calcular_total()
        descuento = total * (porcentaje / 100)
        total_con_descuento = total - descuento
        return total_con_descuento

    def mostrar_carrito(self):
        if not self.productos:
            print("El carrito está vacío.")
            return
        print("Productos en el carrito:")
        for producto, cantidad in self.productos.items():
            print(f"{producto.nombre} - Cantidad: {cantidad}, Precio unitario: ${producto.precio:.2f}")
        print(f"Total sin descuento: ${self.calcular_total():.2f}")     


    