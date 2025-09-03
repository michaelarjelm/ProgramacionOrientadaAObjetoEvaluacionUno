from ejercicio11.clases.empleado import Empleado

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar_empleado(self, nombre, sueldo):
        nuevo = Empleado(nombre, sueldo)
        self.empleados.append(nuevo)
        print(f"Empleado {nombre} contratado con sueldo ${sueldo: }") 

    def listar_empleados(self):
        if not self.empleados:
            print("No hay empleados registrados.")
        else:
            print(f"Lista de empleados en {self.nombre}: ")
            for empleado in self.empleados:
                print(f"- {empleado}")

    def calcular_gasto_total(self):
        total = sum(empleado.sueldo for empleado in self.empleados)
        print(f"- Gasto total en sueldos: ${total: }")
        return total
    
    