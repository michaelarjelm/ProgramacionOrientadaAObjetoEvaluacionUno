from Ejercicio1.LibroBiblioteca import Libro
from Ejercicio1.LibroBiblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    libro1 = Libro("El escarabajo de oro", "Allan Poe", 2)
    libro2 = Libro("Terapia para llevar", "Ana Perez", 1)

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    biblioteca.mostrar_libros()

    biblioteca.prestar_libro("El Principito")
    biblioteca.mostrar_libros()

    biblioteca.devolver_libro("El Principito")
    biblioteca.mostrar_libros()



