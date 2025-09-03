#*****************   Main  ***************************




#**********ejercicio_1: Libro y Biblioteca*************



#***Se importan clases:

# from ejercicio1.clases.biblioteca import Biblioteca
# from ejercicio1.clases.libro import Libro


#***se crean objetos:


# libro1 = Libro("1984","George Orwell",0)
# libro2 = Libro("la metamorfosis","Franz Kafka",0)
# libro3 = Libro("el principito","Antoine de Saint-Exupéry",0)


# mi_biblioteca = Biblioteca()



#****aplicación de métodos:


# mi_biblioteca.agregar_libro(libro1)
# mi_biblioteca.agregar_libro(libro1)
# mi_biblioteca.agregar_libro(libro1)
# mi_biblioteca.agregar_libro(libro2)


# mi_biblioteca.mostrar_lista_libros()


# mi_biblioteca.presta_libro(libro2)


# mi_biblioteca.devolver_libro(libro2)


# mi_biblioteca.mostrar_lista_libros()



#********** ejercicio_2: Curso y Alumno *****************


#***Se importan clases: 



# from ejercicio2.clases.alumno import Alumno
# from ejercicio2.clases.curso import Curso


#*** se crean objetos:



# curso1 = Curso("8-A")


# alumno1 = Alumno("Manuel Gustavo","Abarca Reyes")
# alumno2 = Alumno("Arturo Patricio","Gonzalez Mendez")
# alumno3 = Alumno("Luis Mauricio","Parra Jorquera")
# alumno4 = Alumno("Luis Ignacio","Urra Vergara")


#***aplicación de métodos.


# curso1.inscribir_alumno(alumno1)    
# curso1.inscribir_alumno(alumno2)
# curso1.inscribir_alumno(alumno3)
# curso1.inscribir_alumno(alumno4)


# curso1.listado_alumnos()

# curso1.quitar_alumno()






#******** ejercicio_3: Item y Pedido ***********


#***Se importan clases:*

# from ejercicio3.clases.item import Item
# from ejercicio3.clases.pedido import Pedido


#***se crean objetos.


# mi_pedido = Pedido()


# item1 = Item("globos",30,50)
# item2 = Item("vasos plásticos",100,40)

# producto1 = item1.nombre
# precio1 = item1.precio
# cantidad1 = item1.cantidad

# item1 = Item(producto1,precio1,cantidad1)

# producto2 = item2.nombre
# precio2 = item2.precio
# cantidad2 = item2.cantidad


# item2= Item(producto2,precio2,cantidad2)




#****aplicación de métodos:



# mi_pedido.agregar_item(item1)
# mi_pedido.agregar_item(item2)



# mi_pedido.detalle_pedido()

# print("El total del pedido es: $",mi_pedido.calculo_total())









#**************** ejercicio_4: Sensor ******************



#***Se importa clase:




# from ejercicio4.clases.sensor import Sensor

#***se crea objeto:

# sensor_vibraciones = Sensor("sensor_vibraciones")


#***se aplican métodos:


# sensor_vibraciones.registrar_valores()
# sensor_vibraciones.registrar_valores()
# sensor_vibraciones.registrar_valores()



# sensor_vibraciones.mostrar_mediciones()


# sensor_vibraciones.promedio()

# sensor_vibraciones.maximo()

# sensor_vibraciones.minimo()





#************ ejercicio_5: Catálogo y Película.*********************


#***Se importan clases:


# from ejercicio5.clases.pelicula import Pelicula
# from ejercicio5.clases.catalogo import Catalogo


#***Se crean objetos:

# catalogo_peliculas = Catalogo()


# pelicula1 = Pelicula("Kill Bill","acción", 2003)
# pelicula2 = Pelicula("Cinema Paradiso","drama", 1988)
# pelicula3 = Pelicula("Mulholland drive","thriller",2001)
# pelicula4 = Pelicula("Goodfellas","drama",1990)




#***se aplican métodos:



# catalogo_peliculas.agregar_pelicula(pelicula1)
# catalogo_peliculas.agregar_pelicula(pelicula2)
# catalogo_peliculas.agregar_pelicula(pelicula3)
# catalogo_peliculas.agregar_pelicula(pelicula4)

# catalogo_peliculas.lista_catalogo()


# catalogo_peliculas.busqueda_titulo()


# catalogo_peliculas.filtro_genero()








#*******************  ejercicio_6: Usuario y Autenticación *********************************




#**** Se importan clases:

#**** En este caso, el import de la clase "Usuario" se realiza en el archivo de "autenticacion.py",
#**** ya que la clase "Auth" y sus métodos requieren crear y manejar objetos de "Usuario".



# from ejercicio6.clases.autenticacion import Auth




#****Aplicación de métodos:



# auth = Auth()


# auth.registrar_usuario()


# auth.login()









#***************ejercicio_7: Agenda y Contacto *****************************************

# Crea una clase Contacto con nombre, teléfono y correo. Crea una clase Agenda que permita
# agregar, buscar, eliminar y listar contactos.



#***Se importan clases:
#En este caso, el import de la clase "Contacto" se realiza en el archivo de "agenda.py",
# ya que la clase "Agenda" y sus métodos requieren crear y manejar objetos de "Contacto".



#from ejercicio7.clases.agenda import Agenda


#***Se crea objeto:


# mi_agenda = Agenda()


#***Se aplican métodos:


# mi_agenda.agregar_contacto("Victor", "Vergara", "988854062", "v.vergaran@inacap.cl")
# mi_agenda.agregar_contacto("Michael", "Arjel", "987654321", "m.arjel@inacap.cl")

# mi_agenda.listar_contactos()
# mi_agenda.buscar_contacto()

# mi_agenda.eliminar_contacto()

# mi_agenda.listar_contactos()



#******************* ejercicio_8: Mesa y Restaurante ***************************************



#***Se importan clases:

# from ejercicio8.clases.mesa import Mesa
# from ejercicio8.clases.restaurante import Restaurante


#***Se crean objetos:

# mi_restaurante = Restaurante()


# mesa1 = Mesa(numero = 1, capacidad = 4)
# mesa2 = Mesa(numero = 2, capacidad = 2)
# mesa3 = Mesa(numero = 3, capacidad = 4)



#***Se aplican métodos:


# mi_restaurante.agregar_mesa(mesa1)
# mi_restaurante.agregar_mesa(mesa2)
# mi_restaurante.agregar_mesa(mesa3)
# mi_restaurante.mostrar_estado_mesas()

# mi_restaurante.reservar_mesa(2)

# # mi_restaurante.liberar_mesa(2)

# mi_restaurante.mostrar_estado_mesas()



#********************Ejercicio 9 — Carrito y Producto ****************************




#***Se importan clases:


# from ejercicio9.clases.producto import Producto
# from ejercicio9.clases.carrito import Carro_compras


#***Se crean objetos:

# mi_carrito = Carro_compras()

# producto1 = Producto("alicate universal",3500)
# producto2 = Producto("destornillador punta paleta",2600)
# producto3 = Producto("serrucho carpintero",5800)


#****Se aplican métodos:

# mi_carrito.agregar_producto(producto1, 4)
# mi_carrito.agregar_producto(producto2, 4)
# mi_carrito.agregar_producto(producto3, 2)

# mi_carrito.mostrar_carrito()

# mi_carrito.calcular_total()
# mi_carrito.aplicar_descuento(50)


#********************Ejercicio 10 — Estudiante y Nota*****************************



#En este caso, el import de la clase "Nota" se realiza en el archivo de "estudiante.py",
# ya que la clase "Estudiante" y sus métodos requieren crear y manejar objetos de "Nota".

# from ejercicio10.clases.estudiante import Estudiante


#****Se crea objeto: 


#estudiante = Estudiante("Pablo Vergara")



#****Se aplican métodos:



# estudiante.añadir_nota("Historia y ciencias sociales:", 6.5)
# estudiante.añadir_nota("Lenguaje y comunicación:", 5.5)
# estudiante.añadir_nota("Matemáticas:", 4.0)

# estudiante.calcular_promedio()

# estudiante.mostrar_calificaciones()





# ********************Ejercicio_11 — Empleado y Empresa *******************************



#***Se importan clases:
#En este caso, el import de la clase "Empleado" se realiza en el archivo de "empresa.py",
# ya que la clase "Empresa" y sus métodos requieren crear y manejar objetos de "Empleado".


# from ejercicio11.clases.empresa import Empresa


#****Se crea objeto:

# mi_empresa = Empresa("Vittorio & compañia S.A")





#****Se aplican métodos:


# mi_empresa.contratar_empleado("Ricardo Andráde", 600000)
# mi_empresa.contratar_empleado("Antonio Videla", 750000)
# mi_empresa.contratar_empleado("Roberto Mella", 600000)

# mi_empresa.listar_empleados()

# mi_empresa.calcular_gasto_total()







# *********************Ejercicio_12 — Banco y Cuenta *********************************


#***Se importan clases:
#En este caso, el import de la clase "Cuenta" se realiza en el archivo de "banco.py".
#ya que la clase "Banco" y sus métodos requieren crear y manejar objetos de "Cuenta".

# from ejercicio12.clases.banco import Banco



# banco1 = Banco("Banco Estatal")

# banco1.abrir_cuenta("Verónica Jara", 800000)
# banco1.abrir_cuenta("Alejandra Vergara", 250000)

# banco1.mostrar_estado()

# banco1.transferir("Verónica Jara", "Alejandra Vergara",10000)

# banco1.mostrar_estado()




#*********************** Ejercicio 13 — Veterinaria y Mascotas ***************************


#***Se importan clases
#En este caso, el import de la clase "Mascota", se realiza en el archivo de "veterinaria.py".
# ya que la clase "Veterinaria" y sus métodos requieren crear y manejar objetos de "Mascota".



# from ejercicio13.clases.veterinaria import Veterinaria

#Se crean objetos:


# vetSimi = Veterinaria("Vet Simi")


#***Se aplican métodos:

# vetSimi.registrar_mascota("Canelita","conejo",3)
# vetSimi.registrar_mascota("Rocky","perro",10)
# vetSimi.registrar_mascota("Macaco","gato",5)



# vetSimi.listar_mascotas

# vetSimi.buscar_mascota("rocky")

# vetSimi.calcular_edad_promedio()






#***********************Ejercicio 14 — Exámen y Preguntas.********************************



#***Se importan clases:
#***En este caso, el import de la clase Pregunta se realiza en el archivo de "examen.py".
# ya que la clase "Examen" y sus métodos requieren crear y manejar objetos de "Pregunta".


# from ejercicio14.clases.examen import Examen




#***Se crea objeto:

# examen = Examen("Música-1")





#***Se aplican métodos:


# examen.agregar_pregunta("¿Cuales son la tercera de Do?", "Mi")
# examen.agregar_pregunta("¿Qué letra representa a la nota La en clave americana?","A")
# examen.agregar_pregunta("¿Cuántas son las notas naturales?", "7")

# examen.listar_preguntas()
# examen.contar_preguntas()





