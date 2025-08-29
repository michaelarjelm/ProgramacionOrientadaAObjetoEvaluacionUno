from Ejercicio1.libro import Libro
from Ejercicio1.biblioteca import Biblioteca
from Ejercicio2.alumno import Alumno
from Ejercicio2.curso import Curso
from Ejercicio3.item import Item
from Ejercicio3.pedido import Pedido
# from Ejercicio4.sensor import
# from Ejercicio5.catalogo import
# from Ejercicio5.pelicula import
# from Ejercicio6.auth import
# from Ejercicio6.usuario import
# from Ejercicio7.agenda import
# from Ejercicio7.contacto import
# from Ejercicio8.mesa import
# from Ejercicio8.restaurante import
# from Ejercicio9.carrito import
# from Ejercicio9.producto import
# from Ejercicio10.estudiante import
# from Ejercicio10.nota import
# from Ejercicio11.empleado import
# from Ejercicio11.empresa import
# from Ejercicio12.banco import
# from Ejercicio12.cuenta import
# from Ejercicio13.mascota import
# from Ejercicio13.veterinaria import
# from Ejercicio14.examen import
# from Ejercicio14.pregunta import

# ==== Ejercicio 1: Desarrollo

libro1 = Libro("Nubes de talco", "Amanda Baeza", 5)
libro2 = Libro("Peklo", "Sukinapan", 7)
libro3 = Libro("Tekkonkinkreet", "Taiyo Matsumoto", 3)

bibliobus = Biblioteca()

bibliobus.agregar_libro(libro1)
bibliobus.agregar_libro(libro2)

bibliobus.prestamo(libro1, 3)
bibliobus.devolucion(libro1, 2)
bibliobus.listar_libros()

# ==== Ejercicio 2: Desarrollo

alumno1 = Alumno("Alondra Gonzalez")
alumno2 = Alumno("Rovin Gatica")
alumno3 = Alumno("Diego Foster")

curso = Curso("Ilustracion")

curso.inscribir_alumno(alumno1)
curso.inscribir_alumno(alumno2)

curso.listar_alumnos()

curso.remover_alumno(alumno3)
curso.remover_alumno(alumno1)

# ==== Ejercicio 3: Desarrollo

item1 = Item("lapiz", 1200, 6)
item2 = Item("libreta", 4600, 8)
item3 = Item("pila AA", 800, 4)

pedido1 = Pedido()

pedido1.agregar_item(item1)
pedido1.agregar_item(item2)
pedido1.agregar_item(item3)

pedido1.calcular_total()

# ==== Ejercicio 4: Desarrollo

# ==== Ejercicio 5: Desarrollo

# ==== Ejercicio 6: Desarrollo

# ==== Ejercicio 7: Desarrollo

# ==== Ejercicio 8: Desarrollo

# ==== Ejercicio 9: Desarrollo

# ==== Ejercicio 10: Desarrollo

# ==== Ejercicio 11: Desarrollo

# ==== Ejercicio 12: Desarrollo

# ==== Ejercicio 13: Desarrollo

# ==== Ejercicio 14: Desarrollo
