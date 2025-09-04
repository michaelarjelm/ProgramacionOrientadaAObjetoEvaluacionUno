# ejercicio10/Nota.py
class Nota:
    def __init__(self, asignatura, calificacion):
        self.asignatura = asignatura
        self.calificacion = min(max(1.0, float(calificacion)), 7.0)  # Escala de 1.0 a 7.0