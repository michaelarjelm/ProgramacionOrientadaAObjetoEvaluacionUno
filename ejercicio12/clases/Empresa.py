# Creamos la calse empresa 


from ejercicio12.clases.Empleado import Empleado

class Empresa:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.empleados = []

    def contratar(self, empleado: Empleado):
        self.empleados.append(empleado)

    def listar_empleados(self):
        if not self.empleados:
            print("No hay empleados contratados.")
        else:
            print(f"Empleados de {self.nombre}:")
            for e in self.empleados:
                print(f" - {e}")

    def gasto_total(self) -> float:
        return sum(e.sueldo for e in self.empleados)
