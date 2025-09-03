class Producto:
    """Clase que representa un producto con nombre y precio."""
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
class Carrito:
    """Clase que representa un carrito de compras y gestiona los productos."""
    def __init__(self):
        # La lista contendrá diccionarios con el producto y la cantidad
        self.productos = []
    def agregar_producto(self, producto, cantidad):
        """Agrega un producto con su cantidad al carrito."""
        self.productos.append({"producto": producto, "cantidad": cantidad})
        print(f"✅ Se agregaron {cantidad} unidades de '{producto.nombre}' al carrito.")
    def calcular_total(self):
        """Calcula el costo total del carrito sin descuento."""
        total = 0
        for item in self.productos:
            total += item["producto"].precio * item["cantidad"]
        return total
    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento en porcentaje al total del carrito."""
        if not (0 <= porcentaje <= 100):
            print("❌ El porcentaje de descuento debe estar entre 0 y 100.")
            return None
    
        total_sin_descuento = self.calcular_total()
        descuento = total_sin_descuento * (porcentaje / 100)
        total_con_descuento = total_sin_descuento - descuento
        return total_con_descuento