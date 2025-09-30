class Carrito:
    def __init__(self):
        self.items = {}

    def agregar(self, producto, cantidad=1):
        if producto in self.items:
            self.items[producto] += cantidad
        else:
            self.items[producto] = cantidad

    def total(self):
        return sum(p.precio * c for p, c in self.items.items())

    def total_con_descuento(self, porcentaje):
        total = self.total()
        descuento = total * (porcentaje / 100)
        return total - descuento

    def mostrar(self):
        lista = []
        for p, c in self.items.items():
            lista.append(f"{p.nombre} x{c} = ${p.precio * c:.2f}")
        return lista