from ejercicio01.LibroYBiblioteca import Libro

libroUno = Libro("Orgullo y prejuicio", "Jane Austen", 4)
libroDos = Libro("Twilight","Stephenie Meyer", 2)
libroTres = Libro("El Resplandor", "Stephen King", 0)

#libroUno.consultar()
#libroDos.consultar()
#libroTres.consultar()

from ejercicio01.LibroYBiblioteca import Biblioteca

biblioteca = Biblioteca()
biblioteca.agregarLibro(libroDos)
biblioteca.agregarLibro(libroUno)
biblioteca.agregarLibro(libroTres)

biblioteca.prestarLibro(libroTres)