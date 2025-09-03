# #ejercicio 01 - libro y biblioteca#

# #crando los libros 
# from ejercicio01.desarrollo import Libro, Biblioteca

# libro1 = Libro('Medianoche', 'Claudia Gray', 6)
# libro2 = Libro('Eva Luna', 'Isabel Allende', 8)
# libro3 = Libro('Las brujas del ayer y del mañana', 'Alix Harrow', 0)

# # Creando  Biblioteca
# Mibiblioteca = Biblioteca()

# # Insertando los libros en la biblioteca
# Mibiblioteca.InsertarLibro(libro1)
# Mibiblioteca.InsertarLibro(libro2)
# Mibiblioteca.InsertarLibro(libro3)

# # Prestando un libro con copias
# Mibiblioteca.PrestarLibro(libro2)

# # Prestando el mismo libro de nuevo
# Mibiblioteca.PrestarLibro(libro2)

# # Prestando un libro sin copias
# Mibiblioteca.PrestarLibro(libro3)

# for libro in Mibiblioteca.libros:
#     print(libro.preguntar())




#ejercicio 02 - alumno y curso#

# #Creando alumnos

# from ejercicio02.desarrollo2 import Alumno, Curso

# alumno1 = Alumno('Arya', 'Maldonado')
# alumno2 = Alumno('Atenea', 'Valenzuela')
# alumno3 = Alumno('Finnick', 'Muñoz')
# alumno4 = Alumno('Eren', 'Dugo')

# #creando curso

# CursoCeramica = Curso()

# #agregamos alumnos

# CursoCeramica.agregar_alumno(alumno1)
# CursoCeramica.agregar_alumno(alumno2)
# CursoCeramica.agregar_alumno(alumno3)
# CursoCeramica.agregar_alumno(alumno4)

# #borramos alumnos

# CursoCeramica.retirar_alumno(alumno3)

# #visualizando la lista

# CursoCeramica.lista_alumnos()






# #ejercicio 03 - pedido e item#

# # from ejercicio03.desarrollo3 import Item, Pedido

# # #Clase Item

# # item1 = Item('lima', 500, 20)
# # item2 = Item('corta Uñas', 2990, 10)
# # item3 = Item('esmalte', 5990, 8)

# # #Clase Pedido

# # Mi_pedido = Pedido()

# # #Creando el pedido

# # Mi_pedido.agregar_item(item1)
# # Mi_pedido.agregar_item(item2)
# # Mi_pedido.agregar_item(item3)

# # #Total

# # for item in Mi_pedido.items:
# #     print(f'"{item.nombre}", precio: "{item.precio}", cantidad: "{item.cantidad}", subtotal: "{item.calcular_subtotal}"'())

# # Pedido_total = Mi_pedido.calcular_total()
# # print("Total del pedido:", Pedido_total)






# #ejercicio 04 - sensor y mediciones#


# from ejercicio04.desarrollo4 import Sensor
# #Clase sensor

# Sensor1 = Sensor('sala 1 humedad climatica')
# Sensor2 = Sensor('Sala 2 humedad climatica')

# # registrando humedad climatica

# Sensor1.registrar_medicion (8)
# Sensor2.registrar_medicion (5)

# max_valor = Sensor1.obtener_maximo()
# min_valor = Sensor2.obtener_minimo()

# if max_valor is not None:
#     print(f"El valor máximo es: {max_valor}")
# else:
#     print("No se pueden obtener valores maximos, la lista esta vacia.")







# #ejercicio 05 - pelicula y catalogo#

# from ejercicio05.desarrollo5 import Pelicula, Catalogo


# Pelicula1 = Pelicula('Annabell', 'Terror', 2014)
# Pelicula2 = Pelicula('Los juegos del hambre', 'Accion', 2012)
# Pelicula3 = Pelicula('Silent Hill', 'Misterio', 2006)

# Catalogo_actual = Catalogo ()

# Catalogo_actual.agregar_pelicula(Pelicula1)
# Catalogo_actual.agregar_pelicula(Pelicula2)
# Catalogo_actual.agregar_pelicula(Pelicula3)

# Print(f'este es el listado completo de peliculas')
# Catalogo_actual.listar_todas()






# #ejercicio 06 - usuario y autenticacion simple#

# from ejercicio06.desarrollo6 import Usuario, Auth

# Usuario1 = Usuario('MarciaRojas', 'Marcia')
# Usuario2 = Usuario('Benjamin093', 'pepito')

# Autenticar = Auth()

# Autenticar.registrar_usuario(Usuario1)
# Autenticar.registrar_usuario(Usuario2)

## falta como ejercer el codigo creado ... por un print quizas?






#ejercicio 07 - agenda y contacto#

# from ejercicio07.desarrollo7 import Contacto, Agenda

# Contacto1 = Contacto('maria elena', 987654321,'Mari.ele@gmail.com')
# Contacto2 = Contacto('Carmen berrios', 96932301, 'carmen.ber@gmail.com')

# Mi_agenda = Agenda()

# Mi_agenda.listar_contactos ()

# Buscar_contacto = Mi_agenda.buscar_contacto(Contacto1)

# Mi_agenda.eliminar_contacto(Contacto2)


#ejercicio 08 - restaurante, mesa y reserva#

# from ejercicio08.desarrollo8 import Mesa, Restaurante

# mesa1 = Mesa(8, 10)
# mesa2 = Mesa(1, 2)

# Mi_Restaurante = Restaurante()

# Mi_Restaurante.agregar_mesa(mesa1)
# Mi_Restaurante.agregar_mesa(mesa2)

# Mi_Restaurante.reservar_mesa(mesa2)
# Mi_Restaurante.reservar_mesa(mesa1)

# Mi_Restaurante.mostrar_estado_mesas()

# Mi_Restaurante.liberar_mesa(mesa2)




#ejercicio 09 - carrito con descuento#

# from ejercicio09.desarrollo9 import Producto, Carro

# Producto1 = Producto('arena de gato', 8990)
# Producto2 = Producto('comida de gato', 29990)
# Producto3 = Producto('juguete rascador gato', 5990)

# Mi_carro = Carro()

# Mi_carro.agregar_producto(Producto1, 2)
# Mi_carro.agregar_producto(Producto2, 1)
# Mi_carro.agregar_producto(Producto3, 1)

# print ("tu carro ha obtenido un descuento")
# Mi_carro.aplicar_descuento(15)





#ejercicio 10 - estudiante y nota#

# from ejercicio10.desarrollo10 import Nota, Estudiante

# Nota1 = Nota('Lenguaje', 6,0)
# Nota2 = Nota('Matematica', 5,0)
# Nota3 = Nota('Artes', 6,8)

# Estudiante1 = Estudiante('Margarita')
# Estudiante2 = Estudiante('Carlos')

# Estudiante1.agregar_nota (Nota2)
# Estudiante1.agregar_nota (Nota3)

# Estudiante2.agregar_nota (Nota2)
# Estudiante2.agregar_nota (Nota1)

# Estudiante1.mostrar_calificaciones()
# Estudiante2.mostrar_calificaciones()

# Promedio_final = Estudiante1.calcular_promedio()
# Promedio_final = Estudiante2.calcular_promedio()



# #ejercicio 11 - empleado y empresa#

# from ejercicio11.desarrollo11 import Empleado, Empresa

# # Crear empresa
# Mi_empresa = Empresa()

# # Crear empleados
# Empleado1 = Empleado("Alejandra", 500000)
# Empleado2 = Empleado("Luis", 450000)
# Empleado3 = Empleado("Karla", 800000)

# # Contratar empleados
# Mi_empresa.contratar_empleado(Empleado1)
# Mi_empresa.contratar_empleado(Empleado2)
# Mi_empresa.contratar_empleado(Empleado3)

# # Listar empleados
# Mi_empresa.listar_empleados()

# # Calcular gasto total
# print(f"El gasto total en sueldos es: {Mi_empresa.calcular_gasto_total()}")




# #ejercicio 12 - banco y cuentas#

# from ejercicio12.desarrollo12 import Cuenta, Banco

# Cuenta1 = Cuenta('Rosario Valenzuela', 520000)
# Cuenta2 = Cuenta('Erik Dugo', 610000)
# Cuenta3 = Cuenta('Arya Trinidad', 50000)

# Mi_banco = Banco()

# Mi_banco.abrir_cuenta(Cuenta1)
# Mi_banco.abrir_cuenta(Cuenta3)
# Mi_banco.abrir_cuenta(Cuenta2)

# Mi_banco.mostrar_estado_cuentas()

# Mi_banco.transferir_dinero(Cuenta2, Cuenta3, 80000)

# Mi_banco.mostrar_estado_cuentas()


#ejercicio 13 - veterinaria y mascotas#

# from ejercicio13.desarrollo13 import Mascota, Veterinaria

# Mascota1 = Mascota('Emma','canina, yorkshire', 5)
# Mascota2 = Mascota('Norah', 'felino DLH', 6)
# Mascota3 = Mascota('Aura', 'Huron Marshall', 2)

# Mi_veterinaria = Veterinaria()

# Mi_veterinaria.registrar_mascota(Mascota1)
# Mi_veterinaria.registrar_mascota(Mascota2)
# Mi_veterinaria.registrar_mascota(Mascota3)

# Mi_veterinaria.listar_mascotas()

# mascota_encontrada = Mi_veterinaria.buscar_mascota('Aura')
# if mascota_encontrada:
#         print(f"Mascota encontrada: {mascota_encontrada.nombre}, {mascota_encontrada.especie}, {mascota_encontrada.edad} años")
# else:
#         print("Mascota no encontrada.")

    
# promedio = Mi_veterinaria.calcular_edad_promedio()
    
# if promedio > 0:
#         print(f"La edad promedio de las mascotas es: {promedio:.2f} años")





#ejercicio 14 - examen y preguntas#

from ejercicio14.desarrollo14 import Pregunta, Examen

Pregunta1 = Pregunta('¿ cual es el resultado de cualquier numero dividido por 0?', 0)
Pregunta2 = Pregunta('¿Cual es el resultado de 2x2', 4)

Mi_examen = Examen()

Mi_examen.anadir_pregunta(Pregunta1)
Mi_examen.anadir_pregunta(Pregunta2)

Mi_examen.listar_preguntas()

total_preguntas = Mi_examen.contar_preguntas()
print(f"El examen tiene un total de {total_preguntas} preguntas.")

