
#EJERCICIO 1 : LIBRO Y BIBLIOTECA

from Ejercicio_1.Clases.LibroBiblioteca import Libro, Biblioteca

Libro1 = Libro("El resplandor", "Stephen King", 3)
Libro2 = Libro("It", "Stephen King", 2)
Libro3 = Libro("Carrie", "Stephen King", 1)

#Creo debo agregar mi Biblioteca
biblioteca = Biblioteca([])

#Agregamos algunos libros
biblioteca.agregar(Libro1)
biblioteca.agregar(Libro2)
biblioteca.agregar(Libro3)

#Prestamos
biblioteca.prestar(Libro1)
biblioteca.prestar(Libro2)
biblioteca.prestar(Libro3)
#Qué pasa si vuelvo a pedir un libro sin copias dispo?
biblioteca.prestar(Libro3)

#Devolvemos
biblioteca.devolver(Libro3)
biblioteca.devolver(Libro2)

biblioteca.mostrar()

#----------------------------------------------------------------------------------------------#
#EJERCICIO 2 : ALUMNO Y CURSO

from Ejercicio_2.Clases.AlumnoCurso import Alumno, Curso

Curso1 = Curso("Analista Programador")

Alumno1 = Alumno("Andrea")
Alumno2 = Alumno("Javiera")
Alumno3 = Alumno("Dayane")

Curso1.inscribir(Alumno1)
Curso1.inscribir(Alumno2)
Curso1.inscribir(Alumno3)

Curso1.remover(Alumno1)

Curso1.listar()

#----------------------------------------------------------------------------------------------#
#EJERCICIO 3 : PEDIDO E ITEM

from Ejercicio_3.Clases.PedidoItem import Item, Pedido

Item1 = Item("Gloss", 2000, 20)
Item2 = Item("Sombra de ojos", 10000, 10)
Item3 = Item("Máscar de pestañas", 5000, 15)

pedidobase = Pedido()

costoTotal = Item1.subtotal()
print (f"El subtotal de {Item1.nombre} es: ${costoTotal}")

pedidobase.agregar(Item1)
pedidobase.agregar(Item3)

print (f"El valor total de tu pedido es de: ${pedidobase.total()}")

#----------------------------------------------------------------------------------------------#
#EJERCICIO 4 : SENSOR Y MEDICIONES

from Ejercicio_4.Clases.SensorMediciones import Sensor

nombreSensor = Sensor("Temperatura")

nombreSensor.registrar(10)
nombreSensor.registrar(25)
nombreSensor.registrar(-3)

nombreSensor.promedio()
nombreSensor.maximo()
nombreSensor.minimo()

#----------------------------------------------------------------------------------------------#
#EJERCICIO 5 : PELICULA Y CATALOGO

from Ejercicio_5.Clases.PeliculaCatalogo import Pelicula, Catalogo

mainCatalogo = Catalogo ()

pelicula1 = Pelicula("El Rey León", "Animación", 1994)
pelicula2 = Pelicula("La Sirenita", "Animación", 1989)
pelicula3 = Pelicula("Mulán", "Animación", 1998)

mainCatalogo.agregar(pelicula1)
mainCatalogo.agregar(pelicula2)
mainCatalogo.agregar(pelicula3)

mainCatalogo.filtrar(pelicula1)