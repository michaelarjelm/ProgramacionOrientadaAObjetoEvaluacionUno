class Libro:
    def __init__(self, titulo, autor, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad

    def mostrar_info(self):
        print(f"Titulo: {self.titulo}, Autor: {self.autor}, Cantidad: {self.cantidad}")



class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        for libro in self.libros:
            libro.mostrar_info()
            
    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.cantidad > 0:
                    libro.cantidad -= 1
                    print(f"Se ha prestado el libro: {titulo}")
                else:
                    print(f"El libro: {titulo} no está disponible")
                return
        print(f"El libro: {titulo} no se encuentra en la biblioteca")

