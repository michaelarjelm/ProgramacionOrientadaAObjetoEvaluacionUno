class Ítem:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self):
        """Calcula el subtotal para este ítem (precio * cantidad)."""
        return self.precio * self.cantidad

    def __str__(self):
        return f"Ítem: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | Subtotal: ${self.subtotal():.2f}"

class Pedido:
    def __init__(self):
        self.items = []  # Lista para almacenar los objetos Ítem

    def agregar_item(self, item):
        if isinstance(item, Ítem):
            self.items.append(item)
            print(f"{item.nombre} agregado al pedido")
        else:
            print("Error: Solo se pueden agregar objetos de tipo item")

    def calcular_total(self):
        """Calcula el total de todos los ítems en el pedido"""
        total = 0
        for item in self.items:
            total += item.subtotal()
        return total

    def __str__(self):
        if not self.items:
            return "Pedido vacío"
        
        resumen = "--- Resumen del Pedido ---\n"
        for item in self.items:
            resumen += f"{item}\n"
        resumen += f"---------------------------\n"
        resumen += f"Total del pedido: ${self.calcular_total():.2f}"
        return resumen

# Crear algunos ítems
manzana = Ítem("Manzana", 0.50, 5)
banana = Ítem("Banana", 0.30, 10)
pan = Ítem("Pan", 2.50, 2)

# Crear un pedido
mi_pedido = Pedido()

mi_pedido.agregar_item(manzana)
mi_pedido.agregar_item(banana)
mi_pedido.agregar_item(pan)

# Mostrar el pedido completo
print(mi_pedido)
