# Creamos la Clase Sensor 
class Sensor:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.mediciones = []

    def registrar(self, valor: float):
        # aquie se agraga una nueva medicion...
        self.mediciones.append(valor)

    def promedio(self) -> float:
        # esto nos retorna el promedio de las mediciones 
        if not self.mediciones:
            return 0
        return sum(self.mediciones) / len(self.mediciones)

    def maximo(self) -> float:
        # con esto nos retorna un valor maximo 
        return max(self.mediciones) if self.mediciones else 0

    def minimo(self) -> float:
        # y aqui nos da el valor minimo 
        return min(self.mediciones) if self.mediciones else 0

    def __str__(self) -> str:
        return f"Sensor: {self.nombre}, Mediciones: {self.mediciones}"
