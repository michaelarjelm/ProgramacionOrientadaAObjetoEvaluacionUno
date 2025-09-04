##Crea una clase Libro con título, autor y cantidad de copias. 
##Crea una clase Biblioteca que permita agregar libros, prestar, devolver y mostrar listado de libros.


class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor 
        self.copias = copias 

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
        print(f"-Te hemos prestado el libro: {libro.titulo}")
        return
    
    
    def devolver(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.copias += 1
        print(f"-Has devuelto el libro: {libro.titulo}")
        return 
    def mostrar (self):
        for libro in self.libros:
            print(f"- Titulo del libro: {libro.titulo}")
            print(f"- Autor del libro: {libro.autor}")
            print(f"- Copias disponibles: {libro.copias}")
            
    






