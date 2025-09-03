
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
from ejercicio6.clases.Auth import Auth

if __name__ == "__main__":
    sistema = Auth()
# creamos esta condicion, mientras la condicion sea verdadera.
    while True:
        print("\n--- Sistema de Autenticación ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")
#le damos los valores a las opciones, si indica opcion uno entonses se mostrara el menu para registrarse 
        if opcion == "1":
            usuario = input("Ingrese nombre de usuario: ")
            clave = input("Ingrese contraseña: ")
            if sistema.registrar(usuario, clave):
                print("Usuario registrado con éxito.")
            else:
                print("Ese usuario ya existe.")
# la opcion dos iniciara la sesion con lso datos ya guardados. el else es por si ingreso mal el nombre de usuario o la contarseña de mostrara un mensaje 
# que indique que esta incorrecto 
        elif opcion == "2":
            usuario = input("Usuario: ")
            clave = input("Contraseña: ")
            if sistema.login(usuario, clave):
                print("Inicio de sesión correcto. Bienvenido", usuario)
            else:
                print("Usuario o contraseña incorrectos.")
# opcion tres hace que salga de la condicion y finalice el menu 
# si el ususario ingresa por ejemplo un 4 se mostrara un  mensaje que diga opcion ingresada no valida 
        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción ingresada no válida.")



