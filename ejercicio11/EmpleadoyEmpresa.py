# Creamos la clase empleado
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

# Creamos la empresa
class Empresa:
    def __init__(self):
        self.empleados = []

    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f"Empleado '{empleado.nombre}' se contrata con un sueldo de $'{empleado.sueldo}'.")

    def listar_empleados(self):
        if not self.empleados:
            print("No hay empleados registrados en la empresa.")
            return

        print("\n--- Listado de Empleados ---")
        for empleado in self.empleados:
            print(f"Nombre: '{empleado.nombre}' - Sueldo: $'{empleado.sueldo}'.")

    def gasto_total_sueldos(self):
        if not self.empleados:
            return 0

        total_gastado = sum(empleado.sueldo for empleado in self.empleados)
        return total_gastado