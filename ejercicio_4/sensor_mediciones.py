##Crea una clase Sensor con nombre y una lista de mediciones. 
##Agrega métodos para registrar valores, obtener promedio, máximo y mínimo.

class Sensor:
    def __init__(self, nombre):
       self.nombre = nombre
       self.listaMediciones = []

    def registrar (self, medicion):
        self.listaMediciones.append (medicion)
        print (f"-Se ha registrado una Tº de: {medicion} grados en el sensor {self.nombre} el dia de hoy.")
        
    def promedio (self):
        self.promMedicion = round(sum(self.listaMediciones) / len(self.listaMediciones), 1)
        print (f"- El promedio de hoy es: {self.promMedicion}")    

    def maximo (self):
       self.maxMedicion = max(self.listaMediciones)
       print (f"- El valor máximo de hoy es: {self.maxMedicion}, mantente hidratado.")
    def minimo (self):
       self.minMedicion = min(self.listaMediciones)
       print (f"- El valor mínimo de hoy es: {self.minMedicion}, sal abrigado.")
       
   


  

    

    
