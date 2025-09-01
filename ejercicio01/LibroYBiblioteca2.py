# ~ Construimos la clase Libro    
class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

    def consultar(self):
        print(f"'{self.titulo}', {self.autor}. Número de copias disponibles: {self.copias}.")

# ~ Construimos la clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = [] # ~ Lista para almacenar los libros

    def agregarLibro(self, libro: Libro):
        self.libros.append(libro)
        print(f"¡Has agregado {libro.titulo} a tu biblioteca!")

    def prestarLibro(self, libro: Libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"¡Has retirado {libro.titulo}!")
        else:
            print(f"No existen copias disponibles para retirar :(")

    def devolverLibro(self, libro: Libro):
        self.libros.append(libro)
        print(f"Has devuelto {libro.titulo}. ¡Gracias!")
    
    def listarLibros(self, libro: Libro):
        print("Libros disponibles en la biblioteca:")
        for libro in self.libros:
            libro.consultar()
            