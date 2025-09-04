class Medicion:
    def __init__(self, valor):
        self.valor = float(valor)  # Convierte a float para aceptar numeros decimales
class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mediciones = []

    def registrar_valor(self, valor):
        medicion = Medicion(valor)
        self.mediciones.append(medicion)

    def obtener_promedio(self):
        return sum(m.valor for m in self.mediciones) / len(self.mediciones) if self.mediciones else 0

    def obtener_maximo(self):
        return max(m.valor for m in self.mediciones) if self.mediciones else 0

    def obtener_minimo(self):
        return min(m.valor for m in self.mediciones) if self.mediciones else 0