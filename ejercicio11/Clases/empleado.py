class Empleado:   

    def __init__(self,nombre,sueldo):
        self.nombre=nombre
        self.sueldo=sueldo


    def info(self):
        return (f"{self.nombre}:gana {self.sueldo}")