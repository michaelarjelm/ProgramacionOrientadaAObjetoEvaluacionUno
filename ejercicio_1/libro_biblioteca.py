# ejercicio 1 .py

class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

    def prestar(self):
        if self.copias > 0:
            self.copias -= 1
            return True
        return False

    def devolver(self):
        self.copias += 1

    def __str__(self):
        return f'"{self.titulo}" de {self.autor} — Copias disponibles: {self.copias}'


class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def prestar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
                if libro.prestar():
                    print(f'Se ha prestado el libro: "{libro.titulo}"')
                    return
                else:
                    print(f'No hay copias disponibles de: "{libro.titulo}"')
                    return
        print(f'El libro "{titulo}" no se encuentra en la biblioteca.')

    def devolver_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
                libro.devolver()
                print(f'Se ha devuelto el libro: "{libro.titulo}"')
                return
        print(f'El libro "{titulo}" no pertenece a esta biblioteca.')

    def mostrar_libros(self):
        print("\nCatálogo de la biblioteca:")
        for libro in self.catalogo:
            print(libro)
