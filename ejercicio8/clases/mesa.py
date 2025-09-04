
# Crea una clase Mesa con número, capacidad y estado (ocupada o libre).
class Mesa:
    def __init__(self, numero, capacidad,estado='libre'):
        self.numero = numero
        self.capacidad = capacidad
        self.estado = estado
    def __str__(self):
        return f"Mesa {self.numero}: Capacidad {self.capacidad}, Estado: {self.estado}"
    

