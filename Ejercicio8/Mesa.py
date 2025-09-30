class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            return True
        return False

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            return True
        return False
    
    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Libre"
        return f"Mesa {self.numero} | Capacidad: {self.capacidad} | Estado: {estado}"