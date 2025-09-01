#--------------------------Ejercicio 1-------------------
#from ejercicio1.LibroyBiblioteca import Libro, Biblioteca

#Creamos la biblioteca
#MiBiblioteca = Biblioteca()

#Crearemos el listado de libros disponibles en la biblioteca
#libro1 = Libro('Demon', 'Sam Leó', 5)
#libro2 = Libro('Bully', 'Penelope Douglas', 0)
#libro3 = Libro('Orgullo y prejuicio', 'Jane Austen', 7)

#Agregaremos los libros a la biblioteca
#MiBiblioteca.Insertar(libro1)
#MiBiblioteca.Insertar(libro2)
#MiBiblioteca.Insertar(libro3)

#Listado disponible en la biblioteca
#MiBiblioteca.libros

#Ahora prestaremos un libro
#MiBiblioteca.Prestar(libro1)
#MiBiblioteca.Prestar(libro2)
#MiBiblioteca.Prestar(libro3)

#Devolucion de libro
#MiBiblioteca.Devolucion(libro2)

#Mostramos los libros disponibles en nuestra biblioteca
#MiBiblioteca.VisualizarDisponibilidad()

#-------------------------Ejercicio 2---------------------

#from ejercicio2.AlumnoyCurso import Alumno, Curso

#Creamos el curso
#ClasePython = Curso ("Python")

#Identificamos a los alumnos
#alumno1 = Alumno ('Alan', 'Donoso', 2)
#alumno2 = Alumno ('Damian', 'Espinoza', 3)
#alumno3 = Alumno ('Juan Carlos', 'Alvarez', 1)
#alumno4 = Alumno ('Dayane', 'Palma', 5)
#alumno5 = Alumno ('Alberto', 'Muñoz', 4)

#Agregaos a los alunmos
#ClasePython.AgregarAlumno(alumno1)
#ClasePython.AgregarAlumno(alumno2)
#ClasePython.AgregarAlumno(alumno3)
#ClasePython.AgregarAlumno(alumno4)
#ClasePython.AgregarAlumno(alumno5)

#Hacemos la lista del curso
#ClasePython.ListaAlumnos()

#Eliminamos un alumno de la clase
#ClasePython.RetirarAlumno(alumno4)

#------------------Ejercicio 3---------------------

from ejercicio3.PedidoeÍtem import Pedido, Ítem

#Crear item de pedido
item1 = Ítem("Antonia", 2500, 2)
item2 = Ítem("Alfonso", 1500, 4)
item3 = Ítem("Mariela", 5500, 1)

#Creamos el pedido
Mi_pedido = Pedido()

#Pedido creado
Mi_pedido.agregaritem(item1)
Mi_pedido.agregaritem(item2)
Mi_pedido.agregaritem(item3)

