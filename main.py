#⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚ ~ EJERCICIO 01 ~ ˚.⋆⊹ ࣪ ˖✮｡°⋆˚˖☆⋆˚
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

#⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚ ~ EJERCICIO 02 ~ ˚.⋆⊹ ࣪ ˖✮｡°⋆˚˖☆⋆˚
from ejercicio02.AlumnoYCurso import Alumno, Curso

# ~ Creamos un objeto Curso
miCurso = Curso("Programación Orientada a Objetos", 414)

# ~ Creamos los objetos Alumno
alumnoUno = Alumno("Javiera", 30, 1111)
alumnoDos = Alumno("Andrea", 28, 1112)
alumnoTres = Alumno("Dayane", 29, 1113)
alumnoCuatro = Alumno("Emlia", 31, 1114)

# ~ Inscribimos a los alumnos en el curso
miCurso.inscribirAlumnos(alumnoUno) 
miCurso.inscribirAlumnos(alumnoDos)
miCurso.inscribirAlumnos(alumnoTres)
miCurso.inscribirAlumnos(alumnoCuatro)

# ~ Listamos las niñas inscritas en el curso
miCurso.listarAlumnos(alumnoUno)

# ~ Expulsamos a una por desordenada
miCurso.removerAlumnos(alumnoDos)   
 