# ejercicio11/Empresa.py
class Empresa:
    def __init__(self):
        self.empleados = []

    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)

    def listar_empleados(self):
        for e in self.empleados:
            print(f"Nombre: {e.nombre}, Sueldo: {e.sueldo}")

    def calcular_gasto_total(self):
        return sum(e.sueldo for e in self.empleados) #sum es para sumar todos los sueldos