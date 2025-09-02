#-------------------------------- Ejercicio 1 ---------------------
#from ejercicio1.LibroyBiblioteca import Libro, Biblioteca

# Creamos la biblioteca
#MiBiblioteca = Biblioteca()

# Crearemos el listado de libros disponibles en la biblioteca
#libro1 = Libro('Demon', 'Sam Leó', 5)
#libro2 = Libro('Bully', 'Penelope Douglas', 0)
#libro3 = Libro('Orgullo y prejuicio', 'Jane Austen', 7)

# Agregaremos los libros a la biblioteca
#MiBiblioteca.Insertar(libro1)
#MiBiblioteca.Insertar(libro2)
#MiBiblioteca.Insertar(libro3)

# Listado disponible en la biblioteca
#MiBiblioteca.libros

# Ahora prestaremos un libro
#MiBiblioteca.Prestar(libro1)
#MiBiblioteca.Prestar(libro2)
#MiBiblioteca.Prestar(libro3)

# Devolucion de libro
#MiBiblioteca.Devolucion(libro2)

# Mostramos los libros disponibles en nuestra biblioteca
#MiBiblioteca.VisualizarDisponibilidad()

#-------------------------------- Ejercicio 2 ---------------------

#from ejercicio2.AlumnoyCurso import Alumno, Curso

# Creamos el curso
#ClasePython = Curso ("Python")

# Identificamos a los alumnos
#alumno1 = Alumno ('Alan', 'Donoso', 2)
#alumno2 = Alumno ('Damian', 'Espinoza', 3)
#alumno3 = Alumno ('Juan Carlos', 'Alvarez', 1)
#alumno4 = Alumno ('Dayane', 'Palma', 5)
#alumno5 = Alumno ('Alberto', 'Muñoz', 4)

# Agregaos a los alunmos
#ClasePython.AgregarAlumno(alumno1)
#ClasePython.AgregarAlumno(alumno2)
#ClasePython.AgregarAlumno(alumno3)
#ClasePython.AgregarAlumno(alumno4)
#ClasePython.AgregarAlumno(alumno5)

# Hacemos la lista del curso
#ClasePython.ListaAlumnos()

# Eliminamos un alumno de la clase
#ClasePython.RetirarAlumno(alumno4)

#-------------------------------- Ejercicio 3 ---------------------

#from ejercicio3.PedidoeÍtem import Pedido, Ítem

# Crear item de pedido
#item1 = Ítem("Papas fritas", 2500, 2)
#item2 = Ítem("Nugget", 1500, 4)
#item3 = Ítem("Hamburguesa", 5500, 1)

# Creamos el pedido
#Mi_pedido = Pedido()

# Pedido creado
#print("----Agregar pedidos----")
#Mi_pedido.agregaritem(item1)
#Mi_pedido.agregaritem(item2)
#Mi_pedido.agregaritem(item3)

# Total precio del pedido

#total_final = Mi_pedido.totalpedido()
#print(f'El total de su pedido es: $"{total_final}".')

#------------------------------- Ejercicio 4 ----------------------

#from ejercicio4.SensoryMediciones import Sensor

# Creamos el sensor de marejadas
#Marejadas = Sensor("Sensor de marejada para Playa el Tabo")

# Valores de olas en metros
#Marejadas.registro_valores(0.8)
#Marejadas.registro_valores(3.1)
#Marejadas.registro_valores(2.5)

# Obtener valores y resultados de los sensores de marejadas
#print("-------Resultados de marejadas--------")
#print(f"Mediciones de olas registradas: '{Marejadas.mediciones}' metros.")

# Promedio de las marejadas
#promedio = Marejadas.obtener_promedio()
#print(f"La altura promedio de las olas es: '{promedio:.2}' metros.")

# Marejada maxima
#maxima = Marejadas.maxima()
#print(f"La altura maxima fue de: '{maxima}' metros.")

# Marejada minima
#minima = Marejadas.minima()
#print(f"La altura minoma fue de: '{minima}' metros.")

#------------------------------- Ejercicio 5 -------------------

#from ejercicio5.PelículayCatálogo import Pelicula, Catalogo

# Creamo lista de peliculas que agregaremos con sus generos
#peli1 = Pelicula("101 dalmatas", "Animada", 1961)
#peli2 = Pelicula("IT", "Terror", 2017)
#peli3 = Pelicula("Orgullo y prejucio", "Drama", 2005)
#peli4 = Pelicula("El rey leon", "Animada", 1994)

# Creamos catalogo
#Mi_catalogo = Catalogo()

# Agregar peliculas
#Mi_catalogo.agregar_pelicula(peli1)
#Mi_catalogo.agregar_pelicula(peli2)
#Mi_catalogo.agregar_pelicula(peli3)
#Mi_catalogo.agregar_pelicula(peli4)

# Buscamos alguna pelicula
#Mi_catalogo.buscar_pelicula("La dama y el vagabundon")

# Filtro por genero
#Mi_catalogo.fintro_por_genero("Animada")

# Listado de peliculas
#Mi_catalogo.listado_peliculas()

#-------------------------------  Ejercicio 6 ---------------------

#from ejercicio6.UsuarioyAutenticación import Usuario, Auth

# Crear la clase Auth
#Sistema_auth = Auth()

# Registro de usuarios
#print('-------- Probando el registro------')
#Sistema_auth.registrar_usuario('Dayane_Palma', 'guachupe123')
#Sistema_auth.registrar_usuario('Juan_Perez', 'lacucarracha345')
#Sistema_auth.registrar_usuario('Camila_Alvarez', 'papaya567')
#Sistema_auth.registrar_usuario('Sofia_Navarrete', 'guacamayo789')

# Comprobar inicio de sesion
#print("------- Probando el inicio de sesion------")
#Sistema_auth.login('Juan_Perez', 'lacucarracha345')
#Sistema_auth.login('Sofia_Navarrete', 'guacamayo789')
#Sistema_auth.login('Camila_Alvarez', 'papaya567')
#Sistema_auth.login('Dayane_Palma', 'guachupe123')

# El usuario no existe
#Sistema_auth.login("Felipe Cortes", "contraseña123")

#------------------------------- Ejercicio 7 ------------------------

#from ejercicio7.AgendayContacto import Contacto, Agenda

# Creamos los contactos
#contacto1 = Contacto("Ana Acuña", "987654321", "ana_c@email.com")
#contacto2 = Contacto("Andrea Sepulveda", "123456789", "andrea_s@email.com")
#contacto3 = Contacto("Maria Teresa Castro", "456789123", "maria_c@email.com")

# Creamos la agenda
#Mi_agenda = Agenda()

# Agregar contactos
#Mi_agenda.anadir_contacto(contacto1)
#Mi_agenda.anadir_contacto(contacto2)
#Mi_agenda.anadir_contacto(contacto3)

# Listar todos los contactos
#Mi_agenda.lista_contactos()

# Buscar un contacto
#Mi_agenda.buscar_contacto("Andrea Sepulveda")
#Mi_agenda.buscar_contacto("Luis Sanchez")

# Eliminar un contacto
#Mi_agenda.eliminar_contacto("Ana Acuña")
#Mi_agenda.eliminar_contacto("Luis Sanchez")

# Listar de nuevo para ver el cambio
#Mi_agenda.lista_contactos()

#-------------------------------- Ejercicio 8 ------------------------

#from ejercicio8.RestauranteyMesayReserva import Restaurante, Mesa

# Crear algunas mesas
#mesa1 = Mesa(1, 4)
#mesa2 = Mesa(2, 2)
#mesa3 = Mesa(3, 8)

# Crear el restaurante
#Mi_restaurante = Restaurante()

# Agregar las mesas al restaurante
#Mi_restaurante.agregar_mesa(mesa1)
#Mi_restaurante.agregar_mesa(mesa2)
#Mi_restaurante.agregar_mesa(mesa3)

# Mostrar el estado inicial
#Mi_restaurante.mostrar_estado_mesas()

# Probar la reserva de una mesa
#Mi_restaurante.reservar_mesa(2)
#Mi_restaurante.reservar_mesa(1)

# Intentar reservar una mesa ya ocupada
#Mi_restaurante.reservar_mesa(2)

# Mostrar el estado actualizado
#Mi_restaurante.mostrar_estado_mesas()

# Liberar una mesa
#Mi_restaurante.liberar_mesa(2)

# Intentar liberar una mesa que ya está libre
#Mi_restaurante.liberar_mesa(2)

# Mostrar el estado final
#Mi_restaurante.mostrar_estado_mesas()

#-------------------------------- Ejercicio 9 ------------------------

from ejercicio9.CarritoConDescuento import 
