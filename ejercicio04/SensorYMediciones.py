# ~ Creamos la clase Sensor
class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.medicionesObtenidas = []

    def medicionesObtenidas(self, valor: float):
        self.medicionesObtenidas.append(valor)
        print(f"Sensor {self.nombre}. Valor registrado -> {valor}")

    def promedio(self):
        if not self.medicionesObtenidas:
            return 0.0
        return sum(self.medicionesObtenidas) / len(self.medicionesObtenidas)

    def maximo(self):
        if not self.medicionesObtenidas:
            return 0.0
        return max(self.medicionesObtenidas)

    def minimo(self):
        if not self.medicionesObtenidas:
            return 0.0
        return min(self.medicionesObtenidas)

    def metricas(self):
        print(f"Mediciones obtenidas: {self.nombre}")
        if not self.medicionesObtenidas:
            print("¿Medimos algo? No hay mediciones registradas.")
        else:
            print(f" - Mediciones: {self.medicionesObtenidas}")
            print(f" - Promedio: {self.promedio():.2f}") # Formateado a 2 decimales (:.2f) para que no se alargue tanto como esta prueba :'<
            print(f" - Máximo: {self.maximo()}")
            print(f" - Mínimo: {self.minimo()}")
