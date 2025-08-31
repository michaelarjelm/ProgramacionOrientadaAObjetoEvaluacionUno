class Alumno:
    def __init__(self, nombres, apellidos):
            self.nombres = nombres
            self.apellidos = apellidos
            
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    
    
    
