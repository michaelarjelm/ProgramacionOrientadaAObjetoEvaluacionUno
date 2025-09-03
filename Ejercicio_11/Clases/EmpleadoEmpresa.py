#Crea una clase Empleado con nombre y sueldo. Crea una clase Empresa con lista de empleados.
#Agrega métodos para contratar empleados, listar empleados y calcular el gasto total en sueldos
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
        
        
class Empresa:
    def __init__(self):
        self.listaEmpleados = []
    
    def contratar (self, empleado: Empleado):
        self.listaEmpleados.append(empleado)
        print (f" Has contratado a: {empleado.nombre} con sueldo de: ${empleado.sueldo}")
    def listar (self):
        for empleado in self.listaEmpleados:
            print(f"Nombre del empleado: {empleado.nombre} Sueldo: $ {empleado.sueldo}")
    def gastoTotaSueldos (self):
        totalSueldos = sum(empleado.sueldo for empleado in self.listaEmpleados)
        print (f"El gasto total en sueldos es de: ${totalSueldos}")
        return totalSueldos