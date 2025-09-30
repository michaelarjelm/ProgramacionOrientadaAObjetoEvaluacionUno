from Ejercicio11.Empleado import Empleado

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar(self, nombre, sueldo):
        self.empleados.append(Empleado(nombre, sueldo))

    def listar_empleados(self):
        return [str(e) for e in self.empleados]

    def gasto_total(self):
        return sum(e.sueldo for e in self.empleados) 