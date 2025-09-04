from ejercicio1.Clases.libro import Libro

from ejercicio1.Clases.libro import Libro

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Se ha agregado {libro.titulo} a la biblioteca") 

    def prestar_libro(self, titulo):     
        for libro in self.libros:
            if libro.titulo == titulo and libro.copias > 0:
                libro.copias -= 1
                print(f"Se prestó el libro '{titulo}'. Quedan {libro.copias} copias.")
                return
        print(f"No se pudo prestar '{titulo}'. No hay copias disponibles.")

    def devolver_libro(self, titulo):   
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.copias += 1
                print(f"Se devolvió el libro '{titulo}'. Ahora hay {libro.copias} copias.")
                return
        print(f"El libro '{titulo}' no pertenece a la biblioteca.")

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca")
            return
        print("Libros en la biblioteca:")
        for libro in self.libros:
            print(f"- {libro.titulo} de {libro.autor} ({libro.copias} copias disponibles.)\n")