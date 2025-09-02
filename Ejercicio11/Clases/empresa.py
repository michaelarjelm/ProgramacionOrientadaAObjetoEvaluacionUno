#Clase Empresa

from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio11.Clases.empleado import Empleado

class Empresa:
    def __init__(self):
        self.empleados = []
    
    def contratar(self, nombre, sueldo):
        self.empleados.append(Empleado(nombre, sueldo))
    
    def listar_empleados(self):
        for emple in self.empleados:
            print(f"{emple.nombre} - ${emple.sueldo}")
    
    def gasto_total(self):
        return sum(emple.sueldo for emple in self.empleados)