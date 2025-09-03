##Crea una clase Sensor con nombre y una lista de mediciones. 
##Agrega métodos para registrar valores, obtener promedio, máximo y mínimo.

class Sensor:
    def __init__(self, sensor):
        self.sensor = sensor 
        self.mediciones = []

    def registrar(self, valor):
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
   


    
  

    

    
