# Creamos la clase mesa, con numero, y capacidad 
class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False
# definimos la resarva, verdadero si esta ocupada, falso si esta ocupada 
    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            return True
        return False
# definimos liberar mesa, la misma condicion de arriba 
    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            return True
        return False

    def __str__(self):
        estado = " Lo sentimos la mesa esta ocupada" if self.ocupada else " la mesa esta Libre"
        return f"Mesa {self.numero} (capacidad: {self.capacidad}) - {estado}"
