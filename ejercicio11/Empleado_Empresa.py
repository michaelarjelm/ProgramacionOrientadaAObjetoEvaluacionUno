#Ejercicio 11 — Empleado y Empresa
#Crea una clase Empleado con nombre y sueldo.
#Crea una clase Empresa con lista de empleados.
#Agrega métodos para contratar empleados, listar empleados y calcular el gasto total en sueldos.

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

class Empresa:
    def __init__(self):
        self.empleados = []

    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)

    def listar_empleados(self):
        for empleado in self.empleados:
            print(f"Nombre: {empleado.nombre}, Sueldo: {empleado.sueldo:,.0f}")

    def calcular_gasto_total(self):
        return sum(empleado.sueldo for empleado in self.empleados)
