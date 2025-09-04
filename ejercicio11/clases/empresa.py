
class Empresa:
    def __init__(self):
        self.empleados = []

    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)

    def listar_empleados(self):
        for empleado in self.empleados:
            print(empleado)

    def gasto_total_sueldos(self):
        return sum(empleado.sueldo for empleado in self.empleados)  
    
    