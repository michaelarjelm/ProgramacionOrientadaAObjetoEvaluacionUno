#Clase Mesa
class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.estado = "Libre"
    
    def reservar(self):
        if self.estado == "Libre":
            self.estado == "Ocupada"
            
    def liberar(self):
        if self.estado == "Ocupada":
            self.estado == "Libre"