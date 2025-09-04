class Sensor:
    
    def __init__(self, nombre):
        self.nombre = nombre         
        self.mediciones = []         
    
    
    def registrar(self, valor):
        self.mediciones.append(valor)   
        print(f"Se registró {valor} en el sensor '{self.nombre}'")
    
    
    def promedio(self):
        if len(self.mediciones) == 0:   
            return None
        return sum(self.mediciones) / len(self.mediciones)
    
    
    def maximo(self):
        if len(self.mediciones) == 0:
            return None
        return max(self.mediciones)
    
    
    def minimo(self):
        if len(self.mediciones) == 0:
            return None
        return min(self.mediciones)
    
    
    def mostrar_info(self):
        if len(self.mediciones) == 0:
            print(f"El sensor '{self.nombre}' no tiene datos registrados.")
        else:
            print(f"\nSensor: {self.nombre}")
            print(f"Mediciones: {self.mediciones}")
            print(f"Promedio: {self.promedio():.2f}")
            print(f"Máximo: {self.maximo()}")
            print(f"Mínimo: {self.minimo()}")
            

            


