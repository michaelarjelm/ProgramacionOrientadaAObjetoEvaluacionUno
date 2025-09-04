class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False  # Estado: libre al crear la mesa

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            print(f" Mesa {self.numero} reservada.")
        else:
            print(f" Mesa {self.numero} ya está ocupada.")

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            print(f" Mesa {self.numero} liberada.")
        else:
            print(f" Mesa {self.numero} ya estaba libre.")

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Libre"
        return f"Mesa {self.numero} - Capacidad: {self.capacidad} - Estado: {estado}"
