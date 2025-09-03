
#--------------Ejecicio 1----------------
#     las clases Libro y Biblioteca

from ejercicio1.clases.libro import Libro
from ejercicio1.clases.biblioteca import Biblioteca

if __name__ == "__main__":
    # Crear instancia de la biblioteca
    mi_biblioteca = Biblioteca()

    print("----------------------------------------------------------------------")
    print("Bienvenidos a la Biblioteca de Pirque")
    print("----------------------------------------------------------------------")
    print()

    # Mostrar catálogo inicial
    mi_biblioteca.mostrar_catalogo()
    print()

    # Crear algunos libros
    libro1 = Libro("La liebre y la tortuga", "Aesop", 3)
    libro2 = Libro("Alicia en el País de las Maravillas", "Lewis Carroll", 2)
    libro3 = Libro("La porota", "Antoine de Saint-Exupéry", 1)
    print()

    # Agregar libros a la biblioteca
    mi_biblioteca.agregar_libros(libro1)
    mi_biblioteca.agregar_libros(libro2)
    mi_biblioteca.agregar_libros(libro3)
    print()

    # Mostrar catálogo después de agregar libros
    mi_biblioteca.mostrar_catalogo()
    print()
    
    # Prestar algunos libros
    mi_biblioteca.prestar_libro("La liebre y la tortuga")
    mi_biblioteca.prestar_libro("la porota")
    mi_biblioteca.prestar_libro("Alicia en el País de las Maravillas")
    print()

    # Mostrar catálogo después de prestar libros
    mi_biblioteca.mostrar_catalogo()
    print()

    # Devolver un libro
    mi_biblioteca.devolver_libro("La biblia")
    print() 

    # Mostrar catálogo final
    mi_biblioteca.mostrar_catalogo()
    print()