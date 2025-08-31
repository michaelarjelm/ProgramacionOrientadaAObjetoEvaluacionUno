class Libro:
    def __init__ (self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = int(copias)

    def consultar(self):
        return (f"{self.titulo}, {self.autor}. Número de copias disponibles: {self.copias}.")