from ejercicio1.Clases.libro import Libro
from ejercicio1.Clases.biblioteca import Biblioteca

def main():

    libro1 = Libro("Las aventuras de Alicia en el país de las maravillas", "Lewis Carroll", 1)
    libro2 = Libro("El maravilloso mago de Oz", "L. Frank Bauméry", 2)


    biblioteca = Biblioteca()


    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)


    biblioteca.mostrar_libros()


    biblioteca.prestar_libro("Las aventuras de Alicia en el país de las maravillas")


    biblioteca.devolver_libro("Las aventuras de Alicia en el país de las maravillas")


    biblioteca.mostrar_libros()

if __name__ == "__main__":
    main()

    