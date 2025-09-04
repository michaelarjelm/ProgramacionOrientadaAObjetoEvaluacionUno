class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"\n{libro.titulo} agregado con exito!")

    def prestamo(self, libro, numero_copias: int):
        if libro in self.libros:
            if libro.copias == 0:
                print(f"\nNo hay copias disponibles de {libro.titulo}")
            elif numero_copias > libro.copias:
                print("\nNo hay suficientes copias disponibles")
                print(f"Copias disponibles: {libro.copias}")
            elif numero_copias <= libro.copias:
                libro.copias -= numero_copias
                print(f"\nPrestamo de '{libro.titulo}' realizado con exito!")
                print(f"Copias restantes disponibles: {libro.copias}")
        else:
            print("\nLibro no registrado")
    
    def devolucion(self, libro, numero_copias: int):
        if libro in self.libros:
            libro.copias += numero_copias
            print(f"\n Devolucion de '{libro.titulo}' realizada con exito!")
        else:
            print(f"\nLibro '{libro.titulo}' no registrado")

    def listar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía")
        else:
            print("\n--- Biblioteca ---\n")
            for libro in self.libros:
                print(libro)