class Item:
    """Representa un ítem con nombre, precio y cantidad."""
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def subtotal(self):
        """Calcula el subtotal del ítem."""
        return self.precio * self.cantidad
    def __str__(self):
        """Devuelve una representación en cadena del ítem."""
        return f"{self.nombre} - ${self.precio:.2f} x {self.cantidad} = ${self.subtotal():.2f}"
class Pedido:
    """Representa un pedido que puede contener múltiples ítems."""
    def __init__(self):
        self.items = []
    def agregar_item(self, item):
        """Agrega un ítem al pedido."""
        self.items.append(item)
        print(f"✅ Ítem '{item.nombre}' agregado al pedido.")
    def calcular_total(self):
        """Calcula el total del pedido sumando los subtotales de cada ítem."""
        total = 0
        for item in self.items:
            total += item.subtotal()
        return total
    def mostrar_pedido(self):
        """Muestra un resumen del pedido con todos los ítems y el total."""
        print("\n🧾 Resumen del Pedido:")
        if not self.items:
            print("El pedido está vacío.")
            return
        for item in self.items:
            print(f"  - {item}")
        total_pedido = self.calcular_total()
        print("-" * 30)
        print(f"💰 Total del Pedido: ${total_pedido:.2f}")