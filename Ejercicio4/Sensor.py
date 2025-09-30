class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mediciones = []

    def registrar(self, valor):
        self.mediciones.append(valor)

    def promedio(self):
        if len(self.mediciones) == 0:
            return 0
        return sum(self.mediciones) / len(self.mediciones)

    def maximo(self):
        if len(self.mediciones) == 0:
            return 0
        return max(self.mediciones)

    def minimo(self):
        if len(self.mediciones) == 0:
            return 0
        return min(self.mediciones)