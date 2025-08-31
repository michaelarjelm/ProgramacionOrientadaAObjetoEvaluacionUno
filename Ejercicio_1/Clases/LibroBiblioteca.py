#Crea una clase Libro con título, autor y cantidad de copias. Crea una clase Biblioteca que permita agregar libros, prestar, devolver y mostrar listado de libros.

class Libro:
    def __init__(self, titulo, autor, cantidad_copias):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_copias = cantidad_copias
        self.copias_disponibles = cantidad_copias

    def visualizar(self):
        return (f"{self.titulo} de {self.autor}. Copias disponibles: {self.cantidad_copias}")
    
class Biblioteca:
    def __init__(self, libro: Libro):
        self.listado = []

    def agregar(self, libro):
        self.listado.append(libro)
        print (f"Haz agregado: '{libro.titulo}' de {libro.autor}, a tu Biblioteca. Tienes {libro.cantidad_copias} copias disponibles.")

    def prestar (self, libro):
        if libro.cantidad_copias >0:
            libro.cantidad_copias -=1
            print (f"Haz prestado: '{libro.titulo}' de {libro.autor}, a tu Biblioteca. Tienes {libro.cantidad_copias} copias disponibles.")
        else:
            print (f"No hay copias disponibles de: '{libro.titulo}' de {libro.autor}, en tu Biblioteca.")

    def devolver (self, libro):
        if libro.cantidad_copias < libro.copias_disponibles:
            libro.cantidad_copias +=1
            print (f"Haz devuelto: '{libro.titulo}' de {libro.autor}, a tu Biblioteca. Tienes {libro.cantidad_copias} copias disponibles.")
        else:
            print (f"No puedes devolver este libro, ya que tienes todas las copias disponibles.")
    
    def mostrar(self):
        print("Listado de libros en la Biblioteca:")
        for libro in self.listado:
            print (libro.visualizar())

            