class Nota:
    def __init__(self,asignatura,calificacion):
        self.asignatura=asignatura
        self.calificacion=calificacion

    def __str__(self):
        return f"{self.asignatura}: {self.calificacion}"


        
