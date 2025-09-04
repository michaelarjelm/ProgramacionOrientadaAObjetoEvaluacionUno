class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f"Nombre: {self.nombre}, Sueldo: {self.sueldo}"


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f"¡{empleado.nombre} ha sido contratado/a!")

    def listar_empleados(self):
        if not self.empleados:
            print("La empresa no tiene empleados.")
        else:
            print("Empleados:")
            for empleado in self.empleados:
                print(empleado)

    def calcular_gasto_total_sueldos(self):
        gasto_total = sum(empleado.sueldo for empleado in self.empleados)
        return gasto_total
