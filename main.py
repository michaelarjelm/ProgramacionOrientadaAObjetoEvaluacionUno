 # #⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚ ~ EJERCICIO 01 ~ ˚.⋆⊹ ࣪ ˖✮｡°⋆˚˖☆⋆˚
# from ejercicio01.LibroYBiblioteca2 import Libro, Biblioteca

# # ~ Creamos un objeto Biblioteca
# miBiblioteca = Biblioteca()

# # ~ Creamos los ojetos Libro
# libroUno = Libro("Orgullo y prejuicio", "Jane Austen", 4)
# libroDos = Libro("Twilight", "Stephenie Meyer", 2)
# libroTres = Libro("El Resplandor", "Stephen King", 0)

# # ~ Agregamos los libros a la biblioteca
# miBiblioteca.agregarLibro(libroUno)
# miBiblioteca.agregarLibro(libroDos)
# miBiblioteca.agregarLibro(libroTres)

# # ~ Listamos los libros en la biblioteca
# miBiblioteca.listarLibros()

# # ~ Prestamos un libro
# miBiblioteca.prestarLibro(libroUno)
# miBiblioteca.prestarLibro(libroDos)
# miBiblioteca.prestarLibro(libroTres) # ~ Este es un liblro sin copias disponibles

# # ~ Devolvemos un libro
# miBiblioteca.devolverLibro(libroDos)

# # ~ Listamos los libros en la biblioteca
# miBiblioteca.listarLibros()

# #⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚ ~ EJERCICIO 02 ~ ˚.⋆⊹ ࣪ ˖✮｡°⋆˚˖☆⋆˚
# from ejercicio02.AlumnoYCurso import Alumno, Curso

# # ~ Creamos un objeto Curso
# miCurso = Curso("Programación Orientada a Objetos", 414)

# # ~ Creamos los objetos Alumno
# alumnoUno = Alumno("Javiera", 30, 1111)
# alumnoDos = Alumno("Andrea", 28, 1112)
# alumnoTres = Alumno("Dayane", 29, 1113)
# alumnoCuatro = Alumno("Emlia", 31, 1114)

# # ~ Inscribimos a los alumnos en el curso
# miCurso.inscribirAlumnos(alumnoUno) 
# miCurso.inscribirAlumnos(alumnoDos)
# miCurso.inscribirAlumnos(alumnoTres)
# miCurso.inscribirAlumnos(alumnoCuatro)

# # ~ Listamos las niñas inscritas en el curso
# miCurso.listarAlumnos(alumnoUno)

# # ~ Expulsamos a una por desordenada
# miCurso.removerAlumnos(alumnoDos)   

# #⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚ ~ EJERCICIO 03 ~ ˚.⋆⊹ ࣪ ˖✮｡°⋆˚˖☆⋆˚
# from ejercicio03.PedidoEItem import Item, Pedido

# # ~ Creamos un objeto Item (basado en hechos realesxd)
# itemUno = Item("Centella Tone Brightening Ampoule", 19.990, 2) 
# itemDos = Item("Retinol 0,1% Bakuchiol Cica Serum", 16.490, 1)
# itemTres = Item("VT Vital Cream 50ml", 5590, 4)

# # ~ Consultamos el valor y cantidad disponible de cada item
# print(itemUno.consultar())
# print(itemDos.consultar())   
# print(itemTres.consultar())

# # ~ Creamos un objeto Pedido
# miPedido = Pedido(1)

# # ~ Agregamos los items al pedido
# miPedido.sumarItem(itemUno)
# miPedido.sumarItem(itemDos)
# miPedido.sumarItem(itemTres)    

# # ~ Mostramos la boleta del pedido
# miPedido.boleta()

# # ~ Mostramos el total del pedido
# print(f"Total del pedido: ${miPedido.calcularTotal()}")



# #⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚ ~ EJERCICIO 04 ~ ˚.⋆⊹ ࣪ ˖✮｡°⋆˚˖☆⋆˚
# from ejercicio04.SensorYMediciones import Sensor
# import random

# # ~ Creamos un objeto Sensor
# sensorJavi = Sensor("Bateria") # ZzZzZz

# # ~ Simulamos la obtención de 10 mediciones aleatorias
# for _ in range(10):
#     valorMedido = random.uniform(0, 100)  # Genera un valor float aleatorio entre 0 y 100 (mi porcentaje de batería a esta hora)
#     sensorJavi.medicionesObtenidas(valorMedido) 
# # ~ Mostramos las métricas del sensor
# sensorJavi.metricas()


# #⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚ ~ EJERCICIO 05 ~ ˚.⋆⊹ ࣪ ˖✮｡°⋆˚˖☆⋆˚
# from ejerciocio05.PeliculaYCatalogo import Pelicula, Catalogo

# # ~ Creamos un objeto Catalogo
# miCatalogo = Catalogo()

# # ~ Creamos los objetos Pelicula
# peliculaUno = Pelicula("2001: Odisea del espacio", "Ciencia Ficción", 1968)
# peliculaDos = Pelicula("Batman: El caballero de la noche", "Acción", 2008)
# peliculaTres = Pelicula("Interestelar", "Ciencia Ficción", 2014)
# peliculaCuatro = Pelicula("La La Land", "Musical", 2016)
# peliculaCinco = Pelicula("El Padrino", "Crimen", 1972)

# # ~ Agregamos las películas al catálogo
# miCatalogo.agregarPeliculas(peliculaUno)
# miCatalogo.agregarPeliculas(peliculaDos)
# miCatalogo.agregarPeliculas(peliculaTres)
# miCatalogo.agregarPeliculas(peliculaCuatro)
# miCatalogo.agregarPeliculas(peliculaCinco)

# # ~ Listamos las películas en el catálogo
# miCatalogo.listarPeliculas()

# # ~ Filtramos las películas por género
# miCatalogo.filtrarPorGenero("Ciencia Ficción")
# miCatalogo.filtrarPorGenero("Comedia") # ~ Este género no está en el catálogo

# # ~ Buscamos una película por título
# print(miCatalogo.buscarPorTitulo("Interestelar"))
# print(miCatalogo.buscarPorTitulo("¿Dónde están las rubias?")) # ~ Esta película no está en el catálogo, pero debería xd

# #⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚ ~ EJERCICIO 06 ~ ˚.⋆⊹ ࣪ ˖✮｡°⋆˚˖☆⋆˚
# from ejercicio06.UsuarioYAutenticacion import Usuario, Auth 

# # ~ Creamos un objeto Auth
# sistemaAuth = Auth()

# # ~ Registramos usuarios
# usuarioUno = sistemaAuth.registrarUsuario("Javiera", "password123")
# usuarioDos = sistemaAuth.registrarUsuario("Andrea", "apartejefe123")
# usuarioTres = sistemaAuth.registrarUsuario("Dayane", "abc123xyz")

# # ~ Autenticamos usuarios
# sistemaAuth.autenticarUsuario("Javiera", "password123")  # ~ Credenciales correctas
# sistemaAuth.autenticarUsuario("Andrea", "meleocurriootraidea123")  # ~ Contraseña incorrecta
# sistemaAuth.autenticarUsuario("NonExistentUser", "nopassword")  # ~ Usuario no registrado
# sistemaAuth.autenticarUsuario("Dayane", "abc123xyz")  # ~ Credenciales correctas


# #⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚ ~ EJERCICIO 07 ~ ˚.⋆⊹ ࣪ ˖✮｡°⋆˚˖☆⋆˚
# from ejercicio07.AgendaYContacto import Agenda, Contacto

# # ~ Creamos un objeto Agenda
# miAgenda = Agenda()

# # ~ Creamos los objetos Contacto
# contactoUno = Contacto("Javiera", "964135226", "javi@example.com")
# contactoDos = Contacto("Andrea", "987654321", "andrea@example.com")
# contactoTres = Contacto("Dayane", "954070706", "daya@example.com")

# # ~ Agregamos los contactos a la agenda
# miAgenda.agregarContacto(contactoUno)
# miAgenda.agregarContacto(contactoDos)
# miAgenda.agregarContacto(contactoTres)

# # ~ Mostramos los contactos en la agenda
# miAgenda.mostrarContactos()

# # ~ Buscamos un contacto por nombre
# print(miAgenda.buscarContacto("Andrea"))
# print(miAgenda.buscarContacto("Pepito")) # ~ Este contacto no está en la agenda

# # ~ Eliminamos un contacto por nombre
# miAgenda.eliminarContacto("Dayane")
# miAgenda.eliminarContacto("Juan") # ~ Este contacto no está en la agenda

# # ~ Mostramos los contactos en la agenda después de eliminar
# miAgenda.mostrarContactos()

# #⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚ ~ EJERCICIO 08 ~ ˚.⋆⊹ ࣪ ˖✮｡°⋆˚˖☆⋆˚
# from ejercicio08.RestauranteMesaYReserva import Mesa, Restaurante

# # ~ Creamos un objeto Restaurante
# miRestaurante = Restaurante("Mesa que más aplauda")

# # ~ Creamos los objetos Mesa
# mesaUno = Mesa(1, 4)
# mesaDos = Mesa(2, 2)
# mesaTres = Mesa(3, 6)
# mesaCuatro = Mesa(4, 4)
# mesaCinco = Mesa(5, 8)

# # ~ Agregamos las mesas al restaurante
# miRestaurante.agregarMesa(mesaUno)
# miRestaurante.agregarMesa(mesaDos)
# miRestaurante.agregarMesa(mesaTres)
# miRestaurante.agregarMesa(mesaCuatro)
# miRestaurante.agregarMesa(mesaCinco)

# # ~ Mostramos el estado de las mesas
# miRestaurante.estadoMesas()

# # ~ Reservamos algunas mesas
# miRestaurante.reservar_mesa(2)
# miRestaurante.reservar_mesa(4)
# miRestaurante.reservar_mesa(6) # ~ Esta mesa no existe
# miRestaurante.reservar_mesa(2) # ~ Esta mesa ya está ocupada

# # ~ Mostramos el estado de las mesas después de las reservas
# miRestaurante.estadoMesas()

# # ~ Liberamos una mesa
# miRestaurante.liberarMesa(2)
# miRestaurante.liberarMesa(6) # ~ Esta mesa no existe
# miRestaurante.liberarMesa(2) # ~ Esta mesa ya está libre

# # ~ Mostramos el estado final de las mesas
# miRestaurante.estadoMesas()

#⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚ ~ EJERCICIO 09 ~ ˚.⋆⊹ ࣪ ˖✮｡°⋆˚˖☆⋆˚
# from ejercicio09.CarritoConDescuento import Producto, Carrito   
# # ~ Creamos un objeto Carrito
# miCarrito = Carrito()
# # ~ Creamos los objetos Producto
# productoUno = Producto("Notebook", 499990)
# productoDos = Producto("Smartphone", 259990)
# productoTres = Producto("Audífonos ANC", 54990)

# # ~ Agregamos productos al carrito
# miCarrito.agregarProducto(productoUno, 1)
# miCarrito.agregarProducto(productoDos, 2)
# miCarrito.agregarProducto(productoTres, 3)
# miCarrito.agregarProducto(productoDos, 1) # ~ Agregamos más unidades de un producto ya existente

# # ~ Calculamos el total sin descuento
# totalSinDescuento = miCarrito.calcularTotal()
# print(f"Total sin descuento: ${totalSinDescuento}")

# # ~ Calculamos el total con un descuento del 10%
# totalConDescuento = miCarrito.calcularTotal(descuento=10)
# print(f"Total con descuento del 10%: ${totalConDescuento}")

# # ~ Mostramos el resumen del carrito
# miCarrito.resumenCarrito()

#⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚ ~ EJERCICIO 10 ~ ˚.⋆⊹ ࣪ ˖✮｡°⋆˚˖☆⋆˚
from ejercicio10.EstudianteYNota import Nota, Estudiante    

# ~ Creamos un objeto Estudiante
miEstudiante = Estudiante("Javiera")

# ~ Creamos los objetos Nota
notaUno = Nota("Lenguaje y Comunicación", 6.5)
notaDos = Nota("Matemáticas", 4.0)

# ~ Agregamos notas al estudiante
miEstudiante.agregarNota(notaUno)
miEstudiante.agregarNota(notaDos)

# ~ Mostramos las notas del estudiante
miEstudiante.mostrarNotas()

# ~ Calculamos y mostramos el promedio de las notas
promedioNotas = miEstudiante.promedio()
print(f"Promedio de notas de {miEstudiante.nombre}: {promedioNotas:.2f}")
