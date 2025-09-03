class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.estado = "libre"
        
    def __str__(self):
        return f"Mesa {self.numero} (Capacidad: {self.capacidad}, Estado: {self.estado})"
