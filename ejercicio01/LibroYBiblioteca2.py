class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

    def consultar(self):
        print(f"'{self.titulo}', {self.autor}. Número de copias disponibles: {self.copias}.")
    
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregarLibro(self, libro: Libro):
        self.libros.append(libro)
        print(f"¡Has agregado {libro.titulo} a tu biblioteca!")

    def prestarLibro(self, libro: Libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Has retirado {libro}")
        else:
            print(f"No existen copias disponibles para retirar :(")

    def devolverLibro(self, libro: Libro):
        self.libros.append(libro)
        print(f"Has devuelto {libro}")
    
    def listarLibros(self):
        print("Libros en la biblioteca:")
        for libro in self.libros:
            libro.consultar()
            