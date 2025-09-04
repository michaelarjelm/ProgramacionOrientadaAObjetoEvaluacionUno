class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar(self, empleado):
        self.empleados.append(empleado)
        print(f"Se contrato a '{empleado.nombre}'")

    def listar_empleados(self):
        if self.empleados:
            print("\n--- Lista empleados ---\n")
            for empleado in self.empleados:
                print(f"{empleado.nombre:8}: ${empleado.sueldo}")
        else:
            print("No hay empleado para mostrar")
    
    def calcular_sueldos(self):
        if self.empleados:
            sueldos = []
            for empleado in self.empleados:
                sueldos.append(empleado.sueldo)
            print("\n-- Pago de sueldos --\n")
            print(f"Total a pagar: ${sum(sueldos)}\n")
        else:
            print("No hay sueldos para calcular")