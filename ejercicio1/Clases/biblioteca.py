
from ejercicio1.Clases import libro

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self):
        self.libros.append(libro)
        print("Se ha agregado {libro.titulo} a la biblioteca")

    def prestar_libro (self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Ha prestado el libro {libro.titulo}")
        else:
            print(f"El libro {libro.titulo} no esta disponible")

    def devolver_libro(self, libro):
        self.libros.append(libro)
        print(f"Se ha devuelto el libro {libro.titulo}")


    def mostrar_libros(self):
            if not self.libros:
                print("No hay libros en la biblioteca")
                
                return 
            print("Libros en la biblioteca:")
            for libro in self.libros:
                print(f"- {libro.titulo} de {libro.autor} ({libro.copias} copias disponibles)")
                 
                 