##Crea una clase Libro con título, autor y cantidad de copias. 
##Crea una clase Biblioteca que permita agregar libros, prestar, devolver y mostrar listado de libros.

##creacion de la clase libro.
class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor 
        self.copias = copias 

##creacion de la clase biblioteca.
class Biblioteca:
    print("------Bienvenido a la biblioteca-------")
    def __init__ (self):
        self.libros = []
    def agregar(self, libro):
        self.libros.append(libro)
    def prestar(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.copias > 0:
                    libro.copias -= 1
        print(f"-Te hemos prestado el libro: {libro2.titulo}")
        return
    print("-------------------------------")
               
    def devolver(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.copias += 1
        print(f"-Has devuelto el libro: {libro1.titulo}")
        return 
        print("-------------------------------")
                
    def mostrar (self):
        for libro in self.libros:
            print(f"- Titulo del libro: {libro.titulo}")
            print(f"- Autor del libro: {libro.autor}")
            print(f"- Copias disponibles: {libro.copias}")
            print("------------------------------")

mi_biblioteca = Biblioteca()

libro1 = Libro("Cien años de soledad.", "Gabriel Garcia Marquez.", 5)
libro2 = Libro("El corazon delator.", "Edgar Allan Poe.", 7)
libro3 = Libro("La metamorfosis.", "Franz kafka.",3)

mi_biblioteca.agregar(libro1)
mi_biblioteca.agregar(libro2)
mi_biblioteca.agregar(libro3)

mi_biblioteca.prestar("El corazon delator.")

mi_biblioteca.devolver("Cien años de soledad.")

mi_biblioteca.mostrar()          





