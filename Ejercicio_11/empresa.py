# Ejercicio 11 — Empleado y Empresa 
# Crea una clase Empleado con nombre y sueldo. Crea una clase Empresa con lista de empleados. 
# Agrega métodos para contratar empleados, listar empleados y calcular el gasto total en sueldos. 

from empleado import Empleado

class Empresa:
    def __init__(self):
        self.empleados = []

    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f" Empleado {empleado.nombre} contratado.")

    def listar_empleados(self):
        if not self.empleados:
            print(" No hay empleados en la empresa.")
        else:
            print("\n--- Empleados de la Empresa ---")
            for e in self.empleados:
                print(e)

    def gasto_total_sueldos(self):
        total = sum(e.sueldo for e in self.empleados)
        return total
