# Ejercicio 1 — Libro y Biblioteca 
# Crea una clase Libro con título, autor y cantidad de copias. Crea una clase Biblioteca que permita 
# agregar libros, prestar, devolver y mostrar listado de libros. 



class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f" Se agregó el libro: {libro.titulo}")

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                if libro.copias > 0:
                    libro.copias -= 1
                    print(f" Has prestado el libro: {libro.titulo}")
                    return
                else:
                    print(" No hay copias disponibles de este libro.")
                    return
        print(" El libro no está en la biblioteca.")

    def devolver_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                libro.copias += 1
                print(f" Has devuelto el libro: {libro.titulo}")
                return
        print(" El libro no pertenece a esta biblioteca.")

    def mostrar_libros(self):
        if not self.libros:
            print(" La biblioteca está vacía.")
        else:
            print("\n--- Listado de Libros en la Biblioteca ---")
            for libro in self.libros:
                print(libro)
