# ejercicio11/Empleado.py
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = max(0, float(sueldo))