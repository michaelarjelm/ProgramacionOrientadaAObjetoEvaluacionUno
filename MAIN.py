
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

mainCatalogo.listar()

peliculasAnimacion = mainCatalogo.filtrar("Animación")
print("Películas Tipo Animación:")
if peliculasAnimacion:
    for pelicula in peliculasAnimacion:
        print (f"Título: {pelicula.titulo}, Género: {pelicula.genero}, Año: {pelicula.año}")
else: 
    print("No se encontraron películas de este género")

pelicula_buscada = mainCatalogo.buscar("La Sirenita")
if pelicula_buscada:
    print(f"Película encontrada: {pelicula_buscada.titulo} ({pelicula_buscada.genero}, {pelicula_buscada.año})")
else:
    print("La película no se encontró en el catálogo.")

#----------------------------------------------------------------------------------------------#
#EJERCICIO 6 : USUARIO Y AUTENTICACION

from Ejercicio_6.Clases.UsuarioAutenticacion import Usuario, Auth

usuario1 = Usuario("Abdiaz", "123456789")
autenticacion = Auth()

autenticacion.registrar("javiera","987654321")

autenticacion.login("Abdiaz", "123456789")
autenticacion.login("", "")

#----------------------------------------------------------------------------------------------#
#EJERCICIO 7 : AGENDA Y CONTACTO

from Ejercicio_7.Clases.AgendaContacto import Contacto, Agenda

contacto1 = Contacto("Andrea", "987654321", "andrea@gmail.com")
contacto2 = Contacto("Javiera", "123456789", "javiera@gmail.com")
contacto3 = Contacto("Dayane", "456789123", "dayane@gmail.com")

agenda = Agenda()

agenda.agregar(contacto1)
agenda.agregar(contacto2)
agenda.agregar(contacto3)

buscarContacto = agenda.buscar("javiera")
if buscarContacto:
    print(f"Contacto encontrado: Nombre: {buscarContacto.nombre}, Teléfono: {buscarContacto.telefono}, Correo: {buscarContacto.correo}")
else: 
    print("Contacto no encontrado en tu agenda")

agenda.eliminar("andrea")

agenda.listar()

#----------------------------------------------------------------------------------------------#
#EJERCICIO 8 : RESTAURANTE Y MESAS

from Ejercicio_8.Clases.RestauranteMesaReserva import Mesa, Restaurante

mesa1 = Mesa(1, 4, True)
mesa2 = Mesa(2, 2, True)
mesa3 = Mesa(3, 6, False)

aperturaRestaurante = Restaurante()

aperturaRestaurante.agregar(mesa1)
aperturaRestaurante.agregar(mesa2)
aperturaRestaurante.agregar(mesa3)

aperturaRestaurante.reservar(2)
aperturaRestaurante.reservar(3)
aperturaRestaurante.reservar(4)

#----------------------------------------------------------------------------------------------#
#EJERCICIO 9 : CARRITO Y DESCUENTOS

from Ejercicio_9.Clases.CarritoDescuento import Producto, Carrito

Producto1 = Producto("Gloss", 2000)
Producto2 = Producto("Sombra de ojos", 10000)
Producto3 = Producto("Máscar de pestañas", 5000)

carritoCompra = Carrito()

carritoCompra.agregar(Producto1, 2)
carritoCompra.agregar(Producto2, 1)
carritoCompra.agregar(Producto3, 3)

totalSinDescuento = carritoCompra.calcularTotal()
print(f"El total del carrito es: ${totalSinDescuento}")

totalConDescuento = carritoCompra.descuento(50)
#print (f"El total con descuento aplicado es: $ {totalConDescuento}")

#----------------------------------------------------------------------------------------------#
#EJERCICIO 10 : ESTUDIANTE Y NOTAS

from Ejercicio_10.Clases.EstudianteNota import Nota, Estudiante

nota1 = Nota("Matemáticas", 45)
nota2 = Nota("Historia", 68)
nota3 = Nota("Lenguaje", 70)

listaNotas = Estudiante("Andrea")

listaNotas.agregarNota(nota1)
listaNotas.agregarNota(nota2)
listaNotas.agregarNota(nota3)

listaNotas.promedio()

listaNotas.mostrarNotas()