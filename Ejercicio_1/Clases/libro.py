class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} (Copias disponibles: {self.copias})"
