class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = int(copias)

    def preguntar(self):
        return (f"{self.titulo}, {self.autor}. Cantidad disponible: {self.copias}.")
    
class Biblioteca:
    def __init__(self):
        pass