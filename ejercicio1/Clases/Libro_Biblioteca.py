#Ejercicio 1 — Libro y Biblioteca
#Crea una clase Libro con título, autor y cantidad de copias.
# Crea una clase Biblioteca que permita agregar libros, prestar, devolver y mostrar listado de libros.

class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)


    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.copias > 0:
                    print(f"Se ha prestado una copia de '{titulo}'. Copias restantes: {libro.copias}")
                    libro.copias -= 1
                    return True
                else:
                    print(f"No hay copias disponibles de '{titulo}'.")
                    return False

        print(f"El libro '{titulo}' no se encontró en la biblioteca.")
        return False


    def devolver_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.copias += 1
                print(f"Se ha devuelto una copia de '{titulo}'. Copias ahora: {libro.copias}")
                return True
        print(f"El libro '{titulo}' no se pudo devolver (no encontrado).")
        return False


    def mostrar_libros(self):
        for libro in self.libros:
            print(f"Título: {libro.titulo}, Autor: {libro.autor}, Copias: {libro.copias}")

