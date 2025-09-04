
#--------------Ejecicio 1----------------
#     las clases Libro y Biblioteca

# from ejercicio1.clases.libro import Libro
# from ejercicio1.clases.biblioteca import Biblioteca

# if __name__ == "__main__":
#     # Crear instancia de la biblioteca
#     mi_biblioteca = Biblioteca()

#     print("----------------------------------------------------------------------")
#     print("Bienvenidos a la Biblioteca de Pirque")
#     print("----------------------------------------------------------------------")
#     print()

#     # Mostrar catálogo inicial
#     mi_biblioteca.mostrar_catalogo()
#     print()

#     # Crear algunos libros
#     libro1 = Libro("La liebre y la tortuga", "Aesop", 3)
#     libro2 = Libro("Alicia en el País de las Maravillas", "Lewis Carroll", 2)
#     libro3 = Libro("La porota", "Antoine de Saint-Exupéry", 1)
#     print()

#     # Agregar libros a la biblioteca
#     mi_biblioteca.agregar_libros(libro1)
#     mi_biblioteca.agregar_libros(libro2)
#     mi_biblioteca.agregar_libros(libro3)
#     print()

#     # Mostrar catálogo después de agregar libros
#     mi_biblioteca.mostrar_catalogo()
#     print()
    
#     # Prestar algunos libros
#     mi_biblioteca.prestar_libro("La liebre y la tortuga")
#     mi_biblioteca.prestar_libro("la porota")
#     mi_biblioteca.prestar_libro("Alicia en el País de las Maravillas")
#     print()

#     # Mostrar catálogo después de prestar libros
#     mi_biblioteca.mostrar_catalogo()
#     print()

#     # Devolver un libro
#     mi_biblioteca.devolver_libro("La biblia")
#     print() 

#     # Mostrar catálogo final
#     mi_biblioteca.mostrar_catalogo()
#     print()

#--------------Ejecicio 2----------------

# from ejercicio2.clases.alumno import Alumno
# from ejercicio2.clases.curso import Curso

# if __name__ == "__main__":

#     print("----------------------------------------------------------------------")
#     print("Bienvenidos a los Cursos de programación")
#     print("----------------------------------------------------------------------")
#     print()

# # crear instancia de curso
#     curso_python = Curso("Python")
#     curso_java = Curso("Java")
#     curso_javascript = Curso("JavaScript")  

# # crear instancia de alumno
#     alumno1 = Alumno("Ruth Diaz")
#     alumno2 = Alumno("Alexander Murillo")
#     alumno3 = Alumno("Nancy Marchant")

# #ejecutar metodos del archvo curso.py
#     curso_python.inscribir_alumno(alumno1)
#     curso_python.inscribir_alumno(alumno2)
#     curso_python.inscribir_alumno(alumno3)
#     curso_java.inscribir_alumno(alumno1)
#     curso_javascript.inscribir_alumno(alumno2)
#     print()

#     curso_python.listar_alumnos()
#     print()
#     curso_java.listar_alumnos()
#     print()
#     curso_javascript.listar_alumnos()
#     print()

#     curso_python.remover_alumno(alumno2)
#     print()

#     curso_python.listar_alumnos() 
#     print()    

#--------------Ejecicio 3----------------

# from ejercicio3.clases.item import Item
# from ejercicio3.clases.pedido import Pedido

# if __name__ == "__main__":
#     print("----------------------------------------------------------------------")
#     print("Bienvenidos a Mi Tienda Online")
#     print("----------------------------------------------------------------------")
#     print()

#     pedido1 = Pedido()

#     item1 = Item("Camisa", 20.0, 2)
#     item2 = Item("Pantalones", 40.0, 1)
#     item3 = Item("Zapatos", 60.0, 1)

#     pedido1.agregar_item(item1)
#     pedido1.agregar_item(item2)
#     pedido1.agregar_item(item3)
#     print()

#     pedido1.calcular_total()
#     print()

#     pedido1.listar_items()
#     print()

#--------------Ejecicio 4----------------
# from ejercicio4.clases.sensor import Sensor

# if __name__ == "__main__":
#     print("----------------------------------------------------------------------")
#     print("Bienvenidos al Sistema de Monitoreo de Sensores")
#     print("----------------------------------------------------------------------")
#     print()

#     sensor_temperatura = Sensor("Sensor de Temperatura")

#     sensor_temperatura.registrar_valor(22.5)
#     sensor_temperatura.registrar_valor(23.0)
#     sensor_temperatura.registrar_valor(21.8)
#     sensor_temperatura.registrar_valor(24.1)
#     sensor_temperatura.registrar_valor(22.9)
#     print()

#     promedio = sensor_temperatura.obtener_promedio()
#     maximo = sensor_temperatura.obtener_maximo()
#     minimo = sensor_temperatura.obtener_minimo()

#     print(f"Promedio de mediciones: {promedio:.2f}")
#     print(f"Valor máximo: {maximo}")
#     print(f"Valor mínimo: {minimo}")
#     print()

#--------------Ejecicio 5----------------
# from ejercicio5.clases.pelicula import Pelicula
# from ejercicio5.clases.catalogo import Catalogo

# if __name__ == "__main__":
#     print("----------------------------------------------------------------------")
#     print("Bienvenidos al Catálogo de Blockbuster - Estrenos 2025")
#     print("----------------------------------------------------------------------")
#     print()

#     catalogo = Catalogo()

#     pelicula1 = Pelicula("Avatar 3", "Ciencia Ficción", 2025)
#     pelicula2 = Pelicula("Misión Imposible: Sentencia Final", "Acción", 2025)
#     pelicula3 = Pelicula("Inside Out 2", "Animación", 2025) 
#     pelicula4 = Pelicula("Jurassic World: Renacimiento", "Aventura", 2025)
#     pelicula5 = Pelicula("Downton Abbey 3", "Drama", 2025)

#     catalogo.agregar_pelicula(pelicula1)
#     catalogo.agregar_pelicula(pelicula2)
#     catalogo.agregar_pelicula(pelicula3)
#     catalogo.agregar_pelicula(pelicula4)
#     catalogo.agregar_pelicula(pelicula5)
#     print()

#     print("Listado de todas las películas:")
#     for pelicula in catalogo.listar_todas():
#         print(pelicula)
#     print()

#     genero_filtro = "Drama"
#     print(f"Películas del género '{genero_filtro}':")
#     for pelicula in catalogo.filtrar_por_genero(genero_filtro):
#         print(pelicula)
#     print()

#     titulo_buscar = "Avatar 3"
#     pelicula_encontrada = catalogo.buscar_por_titulo(titulo_buscar)
#     if pelicula_encontrada:
#         print(f"Película encontrada: {pelicula_encontrada}")
#     print()

#--------------Ejecicio 6----------------
# from ejercicio6.clases.auth import Auth
# from ejercicio6.clases.usuario import Usuario

# if __name__ == "__main__":
#     print("----------------------------------------------------------------------")
#     print("Bienvenidos al Sistema de Autenticación")
#     print("----------------------------------------------------------------------")
#     print()

#     auth_system = Auth()

#     auth_system.registrar("ruth", "password123")
#     auth_system.registrar("alexander", "securepass")
#     auth_system.registrar("nancy", "mypassword")
#     print()

#     auth_system.login("ruth", "password123")  
#     print()

#     print("Intento de login con credenciales incorrectas:")
#     auth_system.login("alexander", "wrongpass")  
#     print()

#     auth_system.login("nancy", "mypassword")  
#     print()

 
#--------------Ejecicio 7----------------
from ejercicio7.clases.contacto import Contacto
from ejercicio7.clases.agenda import Agenda     
if __name__ == "__main__":
    print("----------------------------------------------------------------------")
    print("Bienvenidos a la Agenda de Contactos")
    print("----------------------------------------------------------------------")
    print()

    agenda = Agenda()
    contacto1 = Contacto("Ruth Diaz", "123456789", "rdiazmarchant@gmial.com")
    contacto2 = Contacto("Alexander Murillo", "191919191", "Amurillod@gmial.com")

    agenda.agregar_contacto(contacto1)
    agenda.agregar_contacto(contacto2)  
    print()

    agenda.listar_contactos()
    print()

    nombre_buscar = "Ruth Diaz"
    contacto_encontrado = agenda.buscar_contacto(nombre_buscar)
    if contacto_encontrado:
        print(f"Contacto encontrado: {contacto_encontrado}")    
    print()

    agenda.eliminar_contacto("Alexander Murillo")
    print()
    
    #probar contacto no registrado
    agenda.eliminar_contacto("Nancy Marchant")
    print()

    agenda.listar_contactos()
    print()
#--------------Ejecicio 8----------------



                         




# Ejercicio 7 — Agenda y Contacto 
# Crea una clase Contacto con nombre, teléfono y correo. Crea una clase Agenda que permita 
# agregar, buscar, eliminar y listar contactos.

# --------------Ejecicio 8---------------- 
# Ejercicio 8 — Restaurante, Mesa y Reserva 
# Crea una clase Mesa con número, capacidad y estado (ocupada o libre). Crea una clase 
# Restaurante que permita agregar mesas, reservar, liberar y mostrar estado de todas las mesas. 
# Ejercicio 9 — Carrito con Descuento 
# Crea una clase Producto con nombre y precio. Crea una clase Carrito que permita agregar 
# productos con cantidad, calcular total y aplicar un descuento en porcentaje. 
# Ejercicio 10 — Estudiante y Nota 
# Crea una clase Nota con asignatura y calificación. Crea una clase Estudiante con nombre y una lista 
# de notas. Agrega métodos para añadir una nota, calcular el promedio y mostrar todas las 
# calificaciones. 
# Ejercicio 11 — Empleado y Empresa 
# Crea una clase Empleado con nombre y sueldo. Crea una clase Empresa con lista de empleados. 
# Agrega métodos para contratar empleados, listar empleados y calcular el gasto total en sueldos. 
# Ejercicio 12 — Banco y Cuentas 
# Crea una clase Cuenta con titular y saldo. Crea una clase Banco con lista de cuentas. Agrega 
# métodos para abrir cuenta, buscar cuenta por titular, transferir dinero entre cuentas y mostrar 
# estado de todas las cuentas. 
# Ejercicio 13 — Veterinaria y Mascotas 
# Crea una clase Mascota con nombre, especie y edad. Crea una clase Veterinaria que permita 
# registrar mascotas, buscar por nombre, listar todas y calcular la edad promedio de las mascotas. 
# Ejercicio 14 — Examen y Preguntas 
# Crea una clase Pregunta con enunciado y respuesta correcta. Crea una clase Examen con una lista 
# de preguntas. Agrega métodos para añadir preguntas, listar preguntas y contar el total de 
# preguntas del examen.
# from ejercicio5.clases.cuenta_bancaria import CuentaBancaria
# from ejercicio5.clases.cliente import Cliente
