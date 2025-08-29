class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mediciones = []

    def agregar_valor(self, valor):
        self.mediciones.append(valor)

    def promedio(self):
        if self.mediciones:
            return f"{sum(self.mediciones) / len(self.mediciones):.2f}"
        else:
            print("No tienes valores para promediar")
    
    def maximo(self):
        if self.mediciones:
            return max(self.mediciones)
        else:
            print("No tienes valores para mostrar")
    
    def minimo(self):
        if self.mediciones:
            return min(self.mediciones)
        else:
            print("No tienes valores para mostrar")    
