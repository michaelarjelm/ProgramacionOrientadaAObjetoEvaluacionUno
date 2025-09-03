
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>

# # ejercicio uno 
#  Crear clases libro y blibliioteca 

# from ejercicio1.clases.libro import Libro
# from ejercicio1.clases.biblioteca import Biblioteca
# # esta es lka lista de libros 
# biblio = Biblioteca()
# libro1 = Libro(" Un secreto en mi colegio ", " Angelica Dossetti ", 4)
# libro2 = Libro(" No toques a mi madre ", " Herve Mestron ", 3)

# # Aqui se agregan los libros 

# biblio.agregar(libro1)
# biblio.agregar(libro2)

# # accion de prestar o devolver 

# biblio.prestar("Un secreto en mi Colegio")
# biblio.devolver("No toques a mi Madre ")

# biblio.listar()


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>

#ejercicio Dos
# Crear clases Alumno y Clase 

# from para llamar a las clases 
# from ejercicio2.clases.Alumno import Alumno
# from ejercicio2.clases.Curso import Curso
# # nombre curso y nombre alumnos 
# curso = Curso("analistas,programadores Inacap")
# alumno1 = Alumno("Carlos blanco")
# alumno2 = Alumno("Edgar ojeda")

# curso.inscribir(alumno1)
# curso.inscribir(alumno2)
# curso.remover("Carlos")  

# print("Alumnos inscritos:", curso.listar())


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>

#ejercicio numero tres 
#crear clase item y pedido

# from ejercicio3.clases.item import Item
# from ejercicio3.clases.pedido import Pedido

# if __name__ == "__main__":
#     pedido = Pedido()

#     #  Aqui Agregamos productos en la lista 
#     pedido.agregar_item(Item("Pan", 1500, 2))
#     pedido.agregar_item(Item("Bebida", 1200, 3))
#     pedido.agregar_item(Item("Queso Gauda", 2500, 1))

#     # aqui mostramos el detalle del pedido
#     pedido.mostrar_detalle()

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>

# Ejercicio Numero Cuatro


# from ejercicio4.clases.Sensor import Sensor

# if __name__ == "__main__":
#     sensor1 = Sensor("Temperatura")

#     # Registramos valores de temperatura 
#     sensor1.registrar(22.5)
#     sensor1.registrar(24.1)
#     sensor1.registrar(21.9)

#     # Mostramos informacion del promedio, minimo y maximo 
#     print(sensor1)
#     print("Promedio:", sensor1.promedio())
#     print("Máximo:", sensor1.maximo())
#     print("Mínimo:", sensor1.minimo())


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>
#ejercicio Numero Cinco 


# from ejercicio5.clases.Pelicula import Pelicula
# from ejercicio5.clases.Catalogo import Catalogo

# if __name__ == "__main__":
#     catalogo = Catalogo()

#     # este sera nuestro catalogo de peliculas aqui se pueden agreagar, nombre, Genero, Año 
#     catalogo.agregar_pelicula(Pelicula("Matrix", "Ciencia Ficción", 1999))
#     catalogo.agregar_pelicula(Pelicula("Titanic", "Romance", 1997))
#     catalogo.agregar_pelicula(Pelicula("El Padrino", "Drama", 1972))
#     catalogo.agregar_pelicula(Pelicula("Avengers", "Acción", 2012))

#     # enlistamos todas las peliculas 
#     catalogo.listar()

#     # Buscar por título nos traera la pelicula buscada por el titulo, buscara en la lista y comparara titulos...
#     peli = catalogo.buscar_por_titulo("Titanic")
#     if peli:
#         print("\n  Wow Pelicula Encontrada:", peli)
#     else:
#         print("\n Ups!! Pelicula No encontrada.")

#     # Filtrar por género al colocar un genero esto nos devolvera una pelicula del genero buscado...
#     print("\n Películas de Drama:")
#     for peli in catalogo.filtrar_por_genero("Drama"):
#         print(" -", peli)


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>

# Ejercicio Numero seis 

#crear clase usuario y Sistema Usuario 


# creamos el import 
# from ejercicio6.clases.Auth import Auth

# if __name__ == "__main__":
#     sistema = Auth()
# # creamos esta condicion, mientras la condicion sea verdadera.
#     while True:
#         print("\n--- Sistema de Autenticación ---")
#         print("1. Registrar usuario")
#         print("2. Iniciar sesión")
#         print("3. Salir")
#         opcion = input("Elige una opción: ")
# #le damos los valores a las opciones, si indica opcion uno entonses se mostrara el menu para registrarse 
#         if opcion == "1":
#             usuario = input("Ingrese nombre de usuario: ")
#             clave = input("Ingrese contraseña: ")
#             if sistema.registrar(usuario, clave):
#                 print("Usuario registrado con éxito.")
#             else:
#                 print("Ese usuario ya existe.")
# # la opcion dos iniciara la sesion con lso datos ya guardados. el else es por si ingreso mal el nombre de usuario o la contarseña de mostrara un mensaje 
# # que indique que esta incorrecto 
#         elif opcion == "2":
#             usuario = input("Usuario: ")
#             clave = input("Contraseña: ")
#             if sistema.login(usuario, clave):
#                 print("Inicio de sesión correcto. Bienvenido", usuario)
#             else:
#                 print("Usuario o contraseña incorrectos.")
# # opcion tres hace que salga de la condicion y finalice el menu 
# # si el ususario ingresa por ejemplo un 4 se mostrara un  mensaje que diga opcion ingresada no valida 
#         elif opcion == "3":
#             print("Saliendo del sistema...")
#             break

#         else:
#             print("Opción ingresada no válida.")


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>

#Ejercicio Numero 7 


# main.py
# from ejercicio7.clases.Agenda import Agenda

# if __name__ == "__main__":
#     agenda = Agenda()
# # lo mismo que el ejercicio anterior hacemos un menú para guardar, buscar o borarra contacto 
#     while True:
#         print("\n--- Agenda de Contactos ---")
#         print("1. Agregar contacto")
#         print("2. Buscar contacto")
#         print("3. Eliminar contacto")
#         print("4. Listar contactos")
#         print("5. Salir")
#         opcion = input("Elige una opción: ")

#         if opcion == "1":
#             nombre = input("Nombre: ")
#             telefono = input("Teléfono: ")
#             correo = input("Correo: ")
#             if agenda.agregar(nombre, telefono, correo):
#                 print("Contacto agregado correctamente.")
#             else:
#                 print("Ese contacto ya existe.")

#         elif opcion == "2":
#             nombre = input("Nombre a buscar: ")
#             contacto = agenda.buscar(nombre)
#             if contacto:
#                 print("T contacto fue Encontrado:", contacto)
#             else:
#                 print("Ups!! No se encontró ese contacto.")

#         elif opcion == "3":
#             nombre = input("Nombre a eliminar: ")
#             if agenda.eliminar(nombre):
#                 print("El contacto eliminado correctamente2.")
#             else:
#                 print("No se encontró ese contacto.")

#         elif opcion == "4":
#             contactos = agenda.listar()
#             if contactos:
#                 print("\nLista de contactos:")
#                 for c in contactos:
#                     print("-", c)
#             else:
#                 print("Agenda vacía.")

#         elif opcion == "5":
#             print("Saliendo de la agenda...")
#             break

#         else:
#             print("Opción no válida.")



#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>


# Ejercicio número 8 
#Crear Clase Mesa Y Restaurante 

# creamos el from import del restaurante 
# from ejercicio8.clases.Restaurante import Restaurante

# if __name__ == "__main__":
#     restaurante = Restaurante()
# # repetimos el mismo menu de los otros ejercicios, misma dinamica, del while true para que se mantenga el menú. 
#     while True:
#         print("\n--- Restaurante ---")
#         print("1. Agregar mesa")
#         print("2. Reservar mesa")
#         print("3. Liberar mesa")
#         print("4. Mostrar mesas")
#         print("5. Salir")
#         op = input("Opción: ")

#         if op == "1":
#             n = int(input("Número de mesa: "))
#             c = int(input("Capacidad: "))
#             restaurante.agregar_mesa(n, c)
#         elif op == "2":
#             n = int(input("Numero de mesa que desea reservar: "))
#             print("Reservada" if restaurante.reservar(n) else "No disponible")
#         elif op == "3":
#             n = int(input("Mesa a liberar: "))
#             print("Liberada" if restaurante.liberar(n) else "No se pudo liberar")
#         elif op == "4":
#             restaurante.mostrar()
#         elif op == "5":
#             break
#         else:
#             print("Opción inválida")

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>>>>>>>

# ejercicio Numero 9 
# crear clase Producto y carrito de compras 

# en esta ocacion llamamos a las dos clases Producto y carrito 
from ejercicio9.clases.Producto import Producto
from ejercicio9.clases.Carrito import Carrito

if __name__ == "__main__":
    carrito = Carrito()
# igual que lo anterior una vez mas el while y true para mantener el meú aboerto.
    while True:
        print("\nTu Carrito de Compras...")
        print("1. Agregar producto")
        print("2. Mostrar carrito")
        print("3. Calcular total con descuento")
        print("4. Salir")
        op = input("Opción: ")

        if op == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            prod = Producto(nombre, precio)
            carrito.agregar(prod, cantidad)

        elif op == "2":
            carrito.mostrar()

        elif op == "3":
            d = float(input("Porcentaje de descuento: "))
            print("Total con descuento:", carrito.total_con_descuento(d))

        elif op == "4":
            break
        else:
            print("Opción no válida")
