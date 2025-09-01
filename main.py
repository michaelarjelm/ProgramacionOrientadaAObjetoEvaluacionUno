from ejercicio01.LibroYBiblioteca import Libro, Biblioteca

#Creamos los ojetos Libro
libroUno = Libro("Orgullo y prejuicio", "Jane Austen", 4)
libroDos = Libro("Twilight", "Stephenie Meyer", 2)
libroTres = Libro("El Resplandor", "Stephen King", 0)

#Creamos un objeto Biblioteca
miBiblioteca = Biblioteca()
    
miBiblioteca.agregarLibro(libroUno)
miBiblioteca.agregarLibro(libroDos)
miBiblioteca.agregarLibro(libroTres)

miBiblioteca.listarLibros()