#Clase sensor
class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mediciones = []
        
    def agrega(self, valor):
        self.mediciones.append(valor)
        
    def promedio(self):
        if len(self.mediciones) == 0:
            return 0
        suma = 0
        for valor in self.mediciones:
            suma += valor
        return suma / len(self.mediciones)
    
    def maximo(self):
        if len(self.mediciones) == 0:
            return None
        mayor = self.mediciones
        for valor in self.mediciones:
            if valor > mayor:
                mayor = valor
        return mayor
    
    def minimo(self):
        if len(self.mediciones) == 0:
            return None
        menor = self.mediciones
        for valor in self.mediciones:
            if valor < menor:
                menor = valor
        return menor