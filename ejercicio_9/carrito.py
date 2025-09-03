class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        self.productos.append({"producto": producto, "cantidad": cantidad})

    def calcular_total(self):
        total = 0
        for item in self.productos:
            total += item["producto"].precio * item["cantidad"]
        return total

    def aplicar_descuento(self, porcentaje):
        total = self.calcular_total()
        descuento = total * (porcentaje / 100)
        total_con_descuento = total - descuento
        return total_con_descuento

# Ejemplo de uso
# Crear productos
producto1 = Producto("Camiseta", 20)
producto2 = Producto("Pantalón", 50)
producto3 = Producto("Zapatos", 80)

# Crear carrito
mi_carrito = Carrito()

# Agregar productos al carrito
mi_carrito.agregar_producto(producto1, 2)  # 2 camisetas
mi_carrito.agregar_producto(producto2, 1)  # 1 pantalón
mi_carrito.agregar_producto(producto3, 1)  # 1 par de zapatos

# Calcular el total sin descuento
total_sin_descuento = mi_carrito.calcular_total()
print(f"Total sin descuento: {total_sin_descuento}")

# Aplicar un descuento del 10%
total_con_descuento = mi_carrito.aplicar_descuento(10)
print(f"Total con descuento (10%): {total_con_descuento}")
