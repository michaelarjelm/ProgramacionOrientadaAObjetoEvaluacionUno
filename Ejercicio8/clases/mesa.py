class Mesa:
    def __init__(self, numero_mesa, capacidad):
        self.numero_mesa = numero_mesa
        self.capacidad = capacidad
        self.estado = True # True == Liberada, False == Ocupada
    