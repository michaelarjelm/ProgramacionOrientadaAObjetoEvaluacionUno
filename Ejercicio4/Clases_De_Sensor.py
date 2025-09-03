class Sensor:
    """Clase que simula un sensor y gestiona sus mediciones."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.mediciones = []
    def registrar_valor(self, valor):
        """Registra una nueva medición en el sensor."""
        self.mediciones.append(valor)
        print(f"✅ Valor {valor} registrado para el sensor '{self.nombre}'.")
    def obtener_promedio(self):
        """Calcula y devuelve el promedio de las mediciones."""
        if not self.mediciones:
            return 0
        return sum(self.mediciones) / len(self.mediciones)
    def obtener_maximo(self):
        """Devuelve el valor máximo de las mediciones."""
        if not self.mediciones:
            return None
        return max(self.mediciones)
    def obtener_minimo(self):
        """Devuelve el valor mínimo de las mediciones."""
        if not self.mediciones:
            return None
        return min(self.mediciones)