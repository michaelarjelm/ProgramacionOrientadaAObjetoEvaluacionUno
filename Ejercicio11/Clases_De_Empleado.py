class Empleado:
    """Clase que representa a un empleado con nombre y sueldo."""
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    def __str__(self):
        """Devuelve una representación en cadena del empleado."""
        return f"Nombre: {self.nombre}, Sueldo: ${self.sueldo:,.2f}"
class Empresa:
    """Clase que gestiona una lista de empleados."""
    def __init__(self):
        self.empleados = []
    def contratar_empleado(self, empleado):
        """Agrega un empleado a la lista de la empresa."""
        self.empleados.append(empleado)
        print(f"✅ Empleado '{empleado.nombre}' contratado.")
    def listar_empleados(self):
        """Muestra la lista de todos los empleados."""
        print("\n📋 Lista de Empleados:")
        if not self.empleados:
            print("No hay empleados en la empresa.")
            return
        for empleado in self.empleados:
            print(f"- {empleado}")
    def calcular_gasto_total_sueldos(self):
        """Calcula y devuelve la suma total de todos los sueldos."""
        gasto_total = sum(empleado.sueldo for empleado in self.empleados)
        return gasto_total