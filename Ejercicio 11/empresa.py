from empleado import Empleado

class Empresa:
    def __init__(self):
        self.empleados = []

    def contratar_empleado(self, nombre, sueldo):
        nuevo_empleado = Empleado(nombre, sueldo)
        self.empleados.append(nuevo_empleado)
        print(f"Empleado '{nombre}' contratado con sueldo ${sueldo:.2f}.")

    def listar_empleados(self):
        if not self.empleados:
            print("No hay empleados en la empresa.")
            return
        print("Lista de empleados:")
        for empleado in self.empleados:
            print(empleado)

    def calcular_gasto_sueldos(self):
        total = sum(empleado.sueldo for empleado in self.empleados)
        return total
