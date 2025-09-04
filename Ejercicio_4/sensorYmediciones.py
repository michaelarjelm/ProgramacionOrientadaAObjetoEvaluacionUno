# Ejercicio 4 — Sensor y Mediciones 
# Crea una clase Sensor con nombre y una lista de mediciones. Agrega métodos para registrar 
# valores, obtener promedio, máximo y mínimo. 

class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mediciones = []

    def registrar_valor(self, valor):
        self.mediciones.append(valor)
        print(f" Se registró {valor} en el sensor {self.nombre}.")

    def obtener_promedio(self):
        if not self.mediciones:
            return 0
        return sum(self.mediciones) / len(self.mediciones)

    def obtener_maximo(self):
        if not self.mediciones:
            return None
        return max(self.mediciones)

    def obtener_minimo(self):
        if not self.mediciones:
            return None
        return min(self.mediciones)

    def mostrar_mediciones(self):
        if not self.mediciones:
            print(f" El sensor {self.nombre} no tiene mediciones registradas.")
        else:
            print(f"\n--- Mediciones del sensor {self.nombre} ---")
            print("Valores:", self.mediciones)
            print(f"Promedio: {self.obtener_promedio():.2f}")
            print(f"Máximo: {self.obtener_maximo()}")
            print(f"Mínimo: {self.obtener_minimo()}")
