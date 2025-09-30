class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Se agregó el libro: {libro.titulo}")

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro.prestar()
        print(f"El libro '{titulo}' no se encuentra en la biblioteca")
        return False

    def devolver_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                libro.devolver()
                return True
        print(f"El libro '{titulo}' no pertenece a esta biblioteca")
        return False

    def mostrar_libros(self):
        print("\nListado de libros en la biblioteca:")
        for libro in self.libros:
            print(libro)
        if not self.libros:
            print("No hay libros en la biblioteca.")