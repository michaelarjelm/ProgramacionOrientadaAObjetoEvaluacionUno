class Empresa:
    def __init__(self):
        self.empleados = []

    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)
        print(f"El empleado {empleado.nombre} fue contratado.")




    def listar_empleados(self):
        print("Lista de empleados:")
        for empleado in self.empleados:
            print(empleado.nombre)

    
    def gasto_total(self):
        if not self.empleados:  
            print("No hay gastos")
            return 0
        else:
            gastoTotal = sum(empleado.sueldo for empleado in self.empleados)
            return gastoTotal
        
       
    
    




        