# ejercicio1/Biblioteca.py
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def prestar(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.copias > 0:
                    libro.copias -= 1
                    print(f"Prestado: {titulo}")
                else:
                    print(f"No hay copias de {titulo}")
                return
        print(f"Libro no encontrado: {titulo}")

    def devolver(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.copias += 1
                print(f"Devuelto: {titulo}")
                return
        print(f"Libro no encontrado: {titulo}")

    def mostrar_listado(self):
        for libro in self.libros:
            print(f"Título: {libro.titulo}, Autor: {libro.autor}, Copias: {libro.copias}")