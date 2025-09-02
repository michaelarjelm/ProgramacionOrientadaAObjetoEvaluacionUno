class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mediciones = []       
    
    def registro_valores(self, valor):
        self.mediciones.append(valor)
    
    def obtener_promedio(self):
        if not self.mediciones:
            return 0
        return sum(self.mediciones) / len(self.mediciones)
    def maxima(self):
        if not self.mediciones:
            return None
        return max(self.mediciones)
    
    def minima(self):
        if not self.mediciones:
            return None
        return min(self.mediciones)