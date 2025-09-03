#Clase sensor

class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mediciones = []

#Registrando datos
    def registrar_medicion(self, valor):
        self.mediciones.append(valor)

#Calculando promedio

def obtener_promedio(self):
            
        if len(self.mediciones) == 0:
            return 0
        return sum(self.mediciones) / len(self.mediciones)


def obtener_maximo(self):
        
        if len(self.mediciones) == 0:
            return None  
        return max(self.mediciones)

def obtener_minimo(self):
        if len(self.mediciones) == 0:
            return None
        return min(self.mediciones)