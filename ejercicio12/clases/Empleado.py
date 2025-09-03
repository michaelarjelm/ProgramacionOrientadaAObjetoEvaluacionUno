

# creamos la clase empleados--- nombre y sueldo 

class Empleado:
    def __init__(self, nombre: str, sueldo: float):
        self.nombre = nombre    #definimos nombre 
        self.sueldo = sueldo    #definimos sueldo 

    def __str__(self):
        return f"{self.nombre} - Sueldo: ${self.sueldo:,.0f}"
