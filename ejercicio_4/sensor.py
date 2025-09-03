class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mediciones = []  # Lista para almacenar las mediciones

    def registrar_valor(self, valor):
        """Registra un nuevo valor de medición."""
        if isinstance(valor, (int, float)):
            self.mediciones.append(valor)
            print(f"Valor {valor} registrado para el sensor {self.nombre}.")
        else:
            print("Error: Solo se pueden registrar valores numéricos (enteros o flotantes).")

    def obtener_promedio(self):
        """Calcula y devuelve el promedio de las mediciones"""
        if not self.mediciones:
            return 0.0  
        return sum(self.mediciones) / len(self.mediciones)

    def obtener_maximo(self):
        """Encuentra y devuelve el valor máximo de las mediciones"""
        if not self.mediciones:
            return None 
        return max(self.mediciones)

    def obtener_minimo(self):
        """Encuentra y devuelve el valor mínimo de las mediciones"""
        if not self.mediciones:
            return None 
        return min(self.mediciones)

    def __str__(self):
        return f"Sensor: {self.nombre} | Mediciones registradas: {len(self.mediciones)}"

# Crear un sensor de temperatura
sensor_temperatura = Sensor("Temperatura Exterior")

#valores
sensor_temperatura.registrar_valor(22.5)
sensor_temperatura.registrar_valor(23.1)
sensor_temperatura.registrar_valor(21.9)
sensor_temperatura.registrar_valor(24.0)
sensor_temperatura.registrar_valor(22.8)

#información 
print(sensor_temperatura)

 #mostrar estadísticas
print(f"Promedio de temperatura: {sensor_temperatura.obtener_promedio():.2f}°C")
print(f"Temperatura máxima: {sensor_temperatura.obtener_maximo()}°C")
print(f"Temperatura mínima: {sensor_temperatura.obtener_minimo()}°C")

# Intentar registrar un valor no numérico
sensor_temperatura.registrar_valor("calor")
