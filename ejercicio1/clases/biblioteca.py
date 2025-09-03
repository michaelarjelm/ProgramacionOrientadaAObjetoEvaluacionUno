# . Crea una clase Biblioteca que permita 
# agregar libros, prestar, devolver y mostrar listado de libros.
from ejercicio1.clases.libro import Libro

class Biblioteca:
    def __init__(self):
        self.catalogo =[]

    def agregar_libros(self, libro:Libro):
        self.catalogo.append(libro)
        print(f'El libro {libro.titulo} ha sido agregado correctamente a la biblioteca.')

    def prestar_libro(self, titulo:str):
        for libro in self.catalogo:
            if libro.titulo == titulo.upper():
                if libro.copias > 0:
                    libro.copias -= 1
                    print(f'Has prestado el libro: {libro.titulo}')
                    if libro.copias == 0:
                        libro.disponible = False
                    return
                else:
                    print(f'No hay copias disponibles del libro: {libro.titulo}')
                    return
        print(f'El libro "{titulo}" no pertenece a esta biblioteca.')
        

    def devolver_libro(self, titulo:str):
        for libro in self.catalogo:
            if libro.titulo == titulo.upper():
                libro.copias += 1
                libro.disponible = True
                print(f'Has devuelto el libro: {libro.titulo}')
                return
        print(f'El libro "{titulo}" no pertenece a esta biblioteca.')                             

    def mostrar_catalogo(self):
        if not self.catalogo:
            print("El catálogo de la biblioteca está vacío.")
        else:
            print("Catálogo de la biblioteca:")
            for libro in self.catalogo:
                print(libro)
