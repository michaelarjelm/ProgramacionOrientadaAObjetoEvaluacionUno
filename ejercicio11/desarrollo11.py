
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo


class Empresa:
    def __init__(self):
            self.empleados = []

    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f"Empleado {empleado.nombre} contratado.")

    def listar_empleados(self):
        if not self.empleados:
            print("No hay empleados en la empresa.")
            return

        print("\n--- Lista de Empleados ---")
        for empleado in self.empleados:
            print(f"Nombre: {empleado.nombre}, Sueldo: {empleado.sueldo}")
        

    def calcular_gasto_total(self):
        total = sum(empleado.sueldo for empleado in self.empleados)
        return total