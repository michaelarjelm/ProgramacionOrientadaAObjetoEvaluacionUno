# archivo: ejercicio1/libro.py

class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

    def prestar(self):
        if self.copias > 0:
            self.copias -= 1
            return True
        return False

    def devolver(self):
        self.copias += 1


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        self.libros.append(libro)

    def prestar(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro.prestar()
        return False

    def devolver(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.devolver()

    def listar(self):
        for libro in self.libros:
            print(f"{libro.titulo} - {libro.autor} ({libro.copias} copias)")
