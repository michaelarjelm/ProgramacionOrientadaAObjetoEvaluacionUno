class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

    def prestar(self):
        if self.copias > 0:
            self.copias -= 1
            print(f"Se prestó el libro: {self.titulo}")
            return True
        else:
            print(f"No hay copias disponibles de: {self.titulo}")
            return False

    def devolver(self):
        self.copias += 1
        print(f"Se devolvió el libro: {self.titulo}")

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} — Copias disponibles: {self.copias}"