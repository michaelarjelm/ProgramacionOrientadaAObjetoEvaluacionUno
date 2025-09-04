# ejercicio1/Libro.py
class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = max(0, int(copias))  # Convertir a entero y validar