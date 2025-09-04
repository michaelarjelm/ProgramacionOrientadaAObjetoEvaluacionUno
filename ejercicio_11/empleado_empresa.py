##Crea una clase Empleado con nombre y sueldo. 
##Crea una clase Empresa con lista de empleados. Agrega métodos para contratar empleados, listar empleados y calcular el gasto total en sueldos.
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
class Empresa:
    def __init__(self):
        self.empleados = []

    def contratar(self, empleado):
        self.empleados.append(empleado)
        print(f"{empleado.nombre} - ha sido contratado.")

    def listar_empleados(self):
        for e in self.empleados:
            print(f"{e.nombre} - Sueldo: {e.sueldo}")

    def gasto_total_sueldos(self):
        total = sum(e.sueldo for e in self.empleados)
        return total
