# ejercicio8/Mesa.py
class Mesa:
    def __init__(self, numero, capacidad, estado="libre"):
        self.numero = int(numero)
        self.capacidad = max(1, int(capacidad))
        self.estado = estado if estado in ["libre", "ocupada"] else "libre"