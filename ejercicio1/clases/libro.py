# Ejercicio 1 — Libro y Biblioteca
# Crea una clase Libro con título, autor y cantidad de copias. Crea una clase Biblioteca que permita
# agregar libros, prestar, devolver y mostrar listado de libros.

class Libro:
    def __init__(self,titulo,autor,copias):
            self.titulo = titulo
            self.autor = autor
            self.copias = copias
            


# #def menu_biblioteca(biblioteca):
#      while TRUE:
#         print("bienvenido a la Biblioteca")
#         print("1. solicitar libro")
#         print("2. devolver libro")
#         print("3. mostrar libros")
#         print("4. salir")
#         opcion = input("Ingresa la opción que deseas realizar: ")
#         if opcion == "1":
#             titulo = input("ingresa el título del libro a solicitar: ").strip
#             confirmacion = biblioteca.presta_libro(titulo)
#             if confirmacion:
#                 print(f" Se confirma el préstamo del libro {titulo} de manera exitosa")
#             else:
#                 print(f"Lamentablemente, no se pudo efectuar el préstamo del libro {titulo}")

#         elif opcion == "2":
#             titulo = input("ingresa el título del libro que deseas devolver: ").strip
#             confirmacion = biblioteca.devolver_libro(titulo)
#             if confirmacion:
#                 print(f"La devolución del libro {titulo} se ha realizado exitosamente")