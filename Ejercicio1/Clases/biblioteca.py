#Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        self.libros.append(libro)

    def mostrar(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            for libro in self.libros:
                print(libro.mostrar_info())

    def prestamo(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                if libro.ndecopias > 0:
                    libro.ndecopias -= 1
                    print(f"Se ha prestado el libro: {libro.titulo}")
                else:
                    print(f"No hay copias disponibles del libro: {libro.titulo}")
                return
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

    def devolver(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                libro.ndecopias += 1
                print(f"Se ha devuelto el libro: {libro.titulo}")
                return
        print(f"El libro '{titulo}' no pertenece a esta biblioteca.")
