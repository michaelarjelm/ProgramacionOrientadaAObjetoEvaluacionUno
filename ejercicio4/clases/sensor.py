# Ejercicio 4 — Sensor y Mediciones
# Crea una clase Sensor con nombre y una lista de mediciones. Agrega métodos para registrar
# valores, obtener promedio, máximo y mínimo.


class Sensor:
    def __init__(self, nombre):
            self.nombre = nombre
            self.lista_mediciones = []
    
    
    def registrar_valores(self,valor):
        self.lista_mediciones.append(valor)
        
    
    
    def promedio(self):
        if len(self.lista_mediciones) == 0:
            return 0
        
        suma = 0
        for valor in self.lista_mediciones:
            suma += valor
        prom = suma / len(self.lista_mediciones)
        return prom
        
        