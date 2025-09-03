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
#print('\n-------- Probando el registro------')
#Sistema_auth.registrar_usuario('Dayane_Palma', 'guachupe123')
#Sistema_auth.registrar_usuario('Juan_Perez', 'lacucarracha345')
#Sistema_auth.registrar_usuario('Camila_Alvarez', 'papaya567')
#Sistema_auth.registrar_usuario('Sofia_Navarrete', 'guacamayo789')

# Comprobar inicio de sesion
#print("\n------- Probando el inicio de sesion------")
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

# Mostrar el estado actualizado de las mesas
#Mi_restaurante.mostrar_estado_mesas()

# Liberar una mesa
#Mi_restaurante.liberar_mesa(2)

# Intentar liberar una mesa que ya está libre
#Mi_restaurante.liberar_mesa(2)

# Mostrar el estado final
#Mi_restaurante.mostrar_estado_mesas()

#-------------------------------- Ejercicio 9 ------------------------

#from ejercicio9.CarritoConDescuento import Producto, Carrito

# Creamos productos
#computador = Producto("Computador Gamer", 1500)
#teclado = Producto("Teclado Mecánico", 80)
#mouse = Producto("Mouse Inalámbrico", 35)

# Creamos un carrito
#Mi_carrito = Carrito()

# Agregar productos al carrito
#Mi_carrito.agregar_producto(computador, 1)
#Mi_carrito.agregar_producto(teclado, 2)
#Mi_carrito.agregar_producto(mouse, 1)

# Calcular y mostrar el total sin descuento
#total = Mi_carrito.calcular_total()
#print(f"Total del carrito sin descuento: $'{total}'.")

# Aplicamos un descuento del 10%
#total_a_pagar = Mi_carrito.aplicar_descuento(10)
#print(f"Total del carrito con 10% de descuento: $'{total_a_pagar:.2f}'.")

#-------------------------------- Ejercicio 10----------------------------

#from ejercicio10.EstudianteyNota import Estudiante, Nota

# CreamosEstudiantes
#estudiante1 = Estudiante("Dayane Palma")
#estudiante2 = Estudiante("Juan Palma")

# Creamos algunas notas del alumno
#print(f"\n--- Calificaciones obtenidas-----")
#nota1 = Nota("Programacion", 6.5)
#nota2 = Nota("Calculo", 5.0)
#nota3 = Nota("Bases de Datos", 7.0)
#nota4 = Nota("Programacion", 6.0)
#nota5 = Nota("Calculo", 5.8)
#nota6 = Nota("Bases de Datos", 7.0)

# Agregaos las notas al estudiante
#estudiante1.agregar_nota(nota1)
#estudiante1.agregar_nota(nota2)
#estudiante1.agregar_nota(nota3)
#estudiante2.agregar_nota(nota4)
#estudiante2.agregar_nota(nota5)
#estudiante2.agregar_nota(nota6)

# Mostrar todas las notas del alumno
#estudiante1.mostrar_calificaciones()
#estudiante2.mostrar_calificaciones()

# Calcular y mostrar el promedio del alumno
#promedio = estudiante1.calcular_promedio()
#print(f"\nEl promedio total de '{estudiante1.nombre}' es: '{promedio:.2f}'.")
#promedio2 = estudiante2.calcular_promedio()
#print(f"\nEl promedio total de '{estudiante2.nombre}' es: '{promedio2:.2f}'.")

#------------------------------------- Ejercicio 11 -------------------------------

#from ejercicio11.EmpleadoyEmpresa import Empleado, Empresa

# Creamos empresa
#Mi_empresa = Empresa()

# Crear empleados
#print(f"\n-----Posibles empleados------")
#empleado1 = Empleado("Dayane Palma", 1500000)
#empleado2 = Empleado("Juan Perez", 1800000)
#empleado3 = Empleado("Camila Gomez", 1200000)

# Contratar a empleados
#Mi_empresa.contratar_empleado(empleado1)
#Mi_empresa.contratar_empleado(empleado2)
#Mi_empresa.contratar_empleado(empleado3)

# Lista de todos los empleados
#Mi_empresa.listar_empleados()

# Calculamos y mostrar el gasto total
#gasto_mensual = Mi_empresa.gasto_total_sueldos()
#print(f"\n El gasto total en sueldos es de: $'{gasto_mensual}'.")

#------------------------------------- Ejercicio 12 ---------------------------------------

#from ejercicio12.BancoyCuentas import Cuenta, Banco

# #Creamos las cuentas

# Cuenta1 = Cuenta('Javiera Lausseube',820000)
# Cuenta2 = Cuenta('Andrea Diaz', 610000)
# Cuenta3 = Cuenta('Emilia Valenzuela', 500000)

# #Creamos nuestro banco
# Mi_banco = Banco()

# #Creamos las cuentas
# Mi_banco.abrir_cuenta(Cuenta1)
# Mi_banco.abrir_cuenta(Cuenta3)
# Mi_banco.abrir_cuenta(Cuenta2)

# #Mostramos lo disponible en las cuentas
# Mi_banco.mostrar_estado_cuentas()

# #Hacemos una tranferencia
# Mi_banco.transferir_dinero(Cuenta2, Cuenta3, 80000)

#  Estado de las cuentas
# Mi_banco.estado_cuentas()

#------------------------------- Ejercicio 13 --------------------------

# from ejercicio13.VeterinariayMascotas import Mascota, Veterinaria

# #Creamos mascotas
# Mascota1 = Mascota('Emma','canina', 8)
# Mascota2 = Mascota('Gariro', 'felino', 4)
# Mascota3 = Mascota('Rusia', 'Erizo', 1)

# #Creamos la veterinaria
# Mi_veterinaria = Veterinaria()

# Mi_veterinaria.registrar_mascota(Mascota1)
# Mi_veterinaria.registrar_mascota(Mascota2)
# Mi_veterinaria.registrar_mascota(Mascota3)

# #Listamos las mascotas
# Mi_veterinaria.listar_mascotas()


# mascota_encontrada = Mi_veterinaria.buscar_mascota('Aura')
# if mascota_encontrada:
#         print(f"\nMascota encontrada: '{mascota_encontrada.nombre}', '{mascota_encontrada.especie}', '{mascota_encontrada.edad}' años.")
# else:
#         print("Mascota no encontrada.")

#---------------------------------- Ejercicio 14 -----------------------------------

# from ejercicio14.ExamenyPreguntas import Pregunta, Examen

# #Creamos las preguntas
# Pregunta1 = Pregunta('¿ cual es el resultado de cualquier numero dividido por 0?', 0)
# Pregunta2 = Pregunta('¿Cual es el resultado de 2+2', 4)

# Mi_examen = Examen()

# Mi_examen.anadir_pregunta(Pregunta1)
# Mi_examen.anadir_pregunta(Pregunta2)

# Mi_examen.listar_preguntas()

# total_preguntas = Mi_examen.contar_preguntas()
# print(f"\nEl examen tiene un total de '{total_preguntas}' preguntas.")