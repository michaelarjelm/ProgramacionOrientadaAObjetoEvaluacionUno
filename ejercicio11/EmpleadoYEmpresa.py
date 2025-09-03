# ~ Creamos una clase Empleado
class Empleado:
    def __init__(self, nombre: str, sueldo: float):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f"Empleado: {self.nombre} - Sueldo: ${self.sueldo:,.2f}" 

# ~ Creamos una clase Empresa
class Empresa:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.empleados = [] # ~ Lista para almacenar los empleados de la empresa

    def contratarEmpleado(self, empleado: Empleado): # ~ Contrata un nuevo empleado
        self.empleados.append(empleado) # ~ Agrega el empleado a la lista
        print(f"{empleado.nombre} ha sido contratado en {self.nombre}.") # ~ Mensaje de confirmación

    def listarEmpleados(self): # ~ Muestra la lista de empleados
        print(f"Empleados de {self.nombre}:") 
        if not self.empleados:  # Si no hay empleados
            print("Te quedaste sin empleados xd")
        else: # Si hay empleados
            for empleado in self.empleados: # Itera sobre la lista de empleados
                print(f"- {empleado}") # Imprime cada empleado
    
    def gastoEnSueldos(self): 
        gastoTotal = sum(empleado.sueldo for empleado in self.empleados) # ~ Calcula el gasto total en sueldos (suma de los sueldos de todos los empleados)
        print(f"Gasto total en item sueldos: ${gastoTotal:,.2f}") # ~ Muestra el gasto total en sueldos
