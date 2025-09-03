class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carro:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        item = [producto, cantidad]
        self.items.append(item)
        print(f"Se agregaron {cantidad} unidad(es) de '{producto}'.")

    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item[0].precio * item[1]
        return total

    def aplicar_descuento(self, porcentaje):
        total_sin_descuento = self.calcular_total()
        descuento = total_sin_descuento * (porcentaje / 100)
        total_final = total_sin_descuento - descuento

        print(f"El total a pagar es: ${total_final:.3f}")
        