class Libro:
    def __init__(self, titulo, autor, cantidad_copias):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_copias = cantidad_copias

    def __str__(self):
        return f"{self.titulo} - {self.autor} (Copias: {self.cantidad_copias})"
