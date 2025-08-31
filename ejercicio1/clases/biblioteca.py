 # crear clase libros, con estructura ya vista, modelo contructor.
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        self.libros.append(libro)  # .append () agregara un libro.

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
