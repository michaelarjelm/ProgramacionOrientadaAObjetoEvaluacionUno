class Libro:
    def __init__(self, titulo, autor, copias: int):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

    def __str__(self):
        return f"* {self.titulo} -{self.autor}. Copias: {self.copias}"