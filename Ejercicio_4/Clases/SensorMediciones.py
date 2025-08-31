#Crea una clase Sensor con nombre y una lista de mediciones. Agrega métodos para registrar valores, obtener promedio, máximo y mínimo.

class Sensor:
    def __init__(self, nombre):
       self.nombre = nombre
       self.listaMediciones = []

    def registrar (self, medicion):
        self.listaMediciones.append (medicion)
        print (f"Has registrado un valor de {medicion} en el sensor de: {self.nombre} ")

    def promedio (self):
        self.promMedicion = sum(self.listaMediciones) / len(self.listaMediciones)    
        print (f"El promedio es: {self.promMedicion}")    

    def maximo (self):
       self.maxMedicion = max(self.listaMediciones)
       print (f"El valor máximo es: {self.maxMedicion}")
    
    def minimo (self):
        self.minMedicion = min(self.listaMediciones)
        print (f" El valor mínimo es : {self.minMedicion}")