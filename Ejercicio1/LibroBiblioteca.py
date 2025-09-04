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
            if libro.titulo == titulo and libro.copias > 0:
                libro.copias -= 1
                print("Libro prestado:", titulo)
                return
        print("No disponible:", titulo)

    def devolver_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.copias += 1
                print("Libro devuelto:", titulo)
                return
        print("Libro no encontrado:", titulo)

    def mostrar_libros(self):
        for libro in self.libros:
            print(f"{libro.titulo}, {libro.autor} ({libro.copias} copias)")



#Ejercicio 1 — Libro y Biblioteca
#Crea una clase Libro con título, autor y cantidad de copias. 
# Crea una clase Biblioteca que permita agregar libros, prestar, devolver y mostrar listado de libros