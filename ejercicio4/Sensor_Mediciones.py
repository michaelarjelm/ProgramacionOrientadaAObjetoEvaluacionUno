#Ejercicio 4 — Sensor y Mediciones
#Crea una clase Sensor con nombre y una lista de mediciones.
#Agrega métodos para registrar valores, obtener promedio, máximo y mínimo.

class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mediciones = []

    def registrar_medicion(self, valor):
        self.mediciones.append(valor)

    def obtener_promedio(self):
        if not self.mediciones:
            return 0
        return sum(self.mediciones) / len(self.mediciones)

    def obtener_maximo(self):
        if not self.mediciones:
            return 0
        return max(self.mediciones)

    def obtener_minimo(self):
        if not self.mediciones:
            return 0
        return min(self.mediciones)
