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

#⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚ ~ EJERCICIO 03 ~ ˚.⋆⊹ ࣪ ˖✮｡°⋆˚˖☆⋆˚
from ejercicio03.PedidoEItem import Item, Pedido

# ~ Creamos un objeto Item (basado en hechos realesxd)
itemUno = Item("Centella Tone Brightening Ampoule", 19.990, 2) 
itemDos = Item("Retinol 0,1% Bakuchiol Cica Serum", 16.490, 1)
itemTres = Item("VT Vital Cream 50ml", 5590, 4)

# ~ Consultamos el valor y cantidad disponible de cada item
print(itemUno.consultar())
print(itemDos.consultar())   
print(itemTres.consultar())

# ~ Creamos un objeto Pedido
miPedido = Pedido(1)

# ~ Agregamos los items al pedido
miPedido.sumarItem(itemUno)
miPedido.sumarItem(itemDos)
miPedido.sumarItem(itemTres)    

# ~ Mostramos la boleta del pedido
miPedido.boleta()

# ~ Mostramos el total del pedido
print(f"Total del pedido: ${miPedido.calcularTotal()}")
