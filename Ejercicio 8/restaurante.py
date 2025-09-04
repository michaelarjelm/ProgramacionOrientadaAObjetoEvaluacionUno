from mesa import Mesa

class Restaurante:
    def __init__(self):
        self.mesas = []

    def agregar_mesa(self, numero, capacidad):
        if any(mesa.numero == numero for mesa in self.mesas):
            print(f"La mesa {numero} ya existe en el restaurante.")
            return False
        nueva_mesa = Mesa(numero, capacidad)
        self.mesas.append(nueva_mesa)
        print(f"Mesa {numero} agregada con capacidad {capacidad}.")
        return True

    def reservar_mesa(self, numero):
        for mesa in self.mesas:
            if mesa.numero == numero:
                return mesa.reservar()
        print(f"No se encontró la mesa {numero}.")
        return False

    def liberar_mesa(self, numero):
        for mesa in self.mesas:
            if mesa.numero == numero:
                return mesa.liberar()
        print(f"No se encontró la mesa {numero}.")
        return False

    def mostrar_estado_mesas(self):
        if not self.mesas:
            print("No hay mesas en el restaurante.")
            return
        print("Estado de las mesas:")
        for mesa in self.mesas:
            print(mesa)
