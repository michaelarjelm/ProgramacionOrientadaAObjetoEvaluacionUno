from producto import Producto

class Carrito:
    def __init__(self):
        # Guardamos productos como diccionario: producto -> cantidad
        self.items = {}

    def agregar_producto(self, producto, cantidad=1):
        if producto in self.items:
            self.items[producto] += cantidad
        else:
            self.items[producto] = cantidad
        print(f"Agregados {cantidad} '{producto.nombre}' al carrito.")

    def calcular_total(self):
        total = sum(producto.precio * cantidad for producto, cantidad in self.items.items())
        return total

    def aplicar_descuento(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            print("Descuento inválido. Debe estar entre 0 y 100.")
            return 0
        total = self.calcular_total()
        descuento = total * (porcentaje / 100)
        total_con_descuento = total - descuento
        return total_con_descuento

    def mostrar_carrito(self):
        if not self.items:
            print("El carrito está vacío.")
            return
        print("Contenido del carrito:")
        for producto, cantidad in self.items.items():
            print(f"- {producto.nombre}: {cantidad} unidad(es) x ${producto.precio:.2f}")
        print(f"Total: ${self.calcular_total():.2f}")
