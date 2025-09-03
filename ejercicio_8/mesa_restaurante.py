class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.estado = "libre"  # Inicialmente, la mesa está libre

    def ocupar(self):
        if self.estado == "libre":
            self.estado = "ocupada"
            return True
        else:
            return False

    def liberar(self):
        if self.estado == "ocupada":
            self.estado = "libre"
            return True
        else:
            return False

    def __str__(self):
        return f"Mesa {self.numero} (Capacidad: {self.capacidad}, Estado: {self.estado})"


class Restaurante:
    def __init__(self):
        self.mesas = []

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)

    def reservar_mesa(self, numero_mesa):
        for mesa in self.mesas:
            if mesa.numero == numero_mesa:
                if mesa.ocupar():
                    return f"Mesa {numero_mesa} reservada."
                else:
                    return f"Mesa {numero_mesa} ya ocupada."
        return f"Mesa {numero_mesa} no encontrada."

    def liberar_mesa(self, numero_mesa):
        for mesa in self.mesas:
            if mesa.numero == numero_mesa:
                if mesa.liberar():
                    return f"Mesa {numero_mesa} liberada."
                else:
                    return f"Mesa {numero_mesa} ya estaba libre."
        return f"Mesa {numero_mesa} no encontrada."

    def mostrar_estado_mesas(self):
        for mesa in self.mesas:
            print(mesa)
