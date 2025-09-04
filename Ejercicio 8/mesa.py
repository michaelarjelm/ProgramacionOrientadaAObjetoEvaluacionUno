class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False  # Estado: False = libre, True = ocupada

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            print(f"Mesa {self.numero} reservada.")
            return True
        else:
            print(f"Mesa {self.numero} ya está ocupada.")
            return False

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            print(f"Mesa {self.numero} liberada.")
            return True
        else:
            print(f"Mesa {self.numero} ya está libre.")
            return False

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Libre"
        return f"Mesa {self.numero} - Capacidad: {self.capacidad} - Estado: {estado}"
