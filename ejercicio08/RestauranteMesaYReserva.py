# Ejercicio 8 — Restaurante, Mesa y Reserva
# Crea una clase Mesa con número, capacidad y estado (ocupada o libre). Crea una clase
# Restaurante que permita agregar mesas, reservar, liberar y mostrar estado de todas las mesas.

# ~ Creamos la clase Mesa
class Mesa:
    def __init__(self, numero, capacidad, libre = True):
        self.numero = numero
        self.capacidad = capacidad
        self.libre = True

    def reservar(self):
        if self.libre:
            self.libre = False
            return True
        return False

    def liberar(self):
        self.libre = True

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mesas = []

    def agregarMesa(self, mesa: Mesa):
        self.mesas.append(mesa)
        print(f"Mesa {mesa.numero} que más aplauda.")

    def reservar_mesa(self, numero):
        for mesa in self.mesas:
            if mesa.numero == numero:
                if not mesa.ocupada:
                    mesa.ocupada = True
                    print(f"Mesa {numero} reservada con éxito!")
                else:
                    print(f"La mesa {numero} ya está ocupada :c")
                return
        print(f"Mesa {numero} no encontrada :o")

    def liberarMesa(self, numero):
        for mesa in self.mesas:
            if mesa.numero == numero:
                if mesa.ocupada:
                    mesa.ocupada = False
                    print(f"Mesa {numero} liberada.")
                else:
                    print(f"La mesa {numero} ya está libre.")
                return
        print(f"No se encontró la mesa {numero}.")

    def estadoMesas(self):
        for mesa in self.mesas:
            print(f"  - {mesa}")
            estado = "Libre" if mesa.libre else "Ocupada"
            print(f"Mesa {mesa.numero} - Capacidad: {mesa.capacidad} - Estado: {estado}")