from ejercicio01.LibroYBiblioteca2 import Libro, Biblioteca

# ~ Creamos un objeto Biblioteca
miBiblioteca = Biblioteca()

# ~ Creamos los ojetos Libro
libroUno = Libro("Orgullo y prejuicio", "Jane Austen", 4)
libroDos = Libro("Twilight", "Stephenie Meyer", 2)
libroTres = Libro("El Resplandor", "Stephen King", 0)

# ~ Agregamos los libros a la biblioteca
miBiblioteca.agregarLibro(libroUno)
miBiblioteca.agregarLibro(libroDos)
miBiblioteca.agregarLibro(libroTres)

# ~ Listamos los libros en la biblioteca
miBiblioteca.listarLibros()

# ~ Prestamos un libro
miBiblioteca.prestarLibro(libroUno)
miBiblioteca.prestarLibro(libroDos)
miBiblioteca.prestarLibro(libroTres) # ~ Este es un liblro sin copias disponibles

# ~ Devolvemos un libro
miBiblioteca.devolverLibro(libroDos)

# ~ Listamos los libros en la biblioteca
miBiblioteca.listarLibros()
