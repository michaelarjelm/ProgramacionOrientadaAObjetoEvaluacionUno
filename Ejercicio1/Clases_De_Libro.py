class Libro:
    """Representa un libro con su título, autor y número de copias."""
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias
    def __str__(self):
        """Devuelve una representación en cadena del libro."""
        return f"'{self.titulo}' por {self.autor}, Copias disponibles: {self.copias}"
class Biblioteca:
    """Permite gestionar una colección de libros."""
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        """Agrega un libro a la biblioteca."""
        self.libros.append(libro)
        print(f"✅ Libro '{libro.titulo}' agregado a la biblioteca.")
    def prestar_libro(self, titulo):
        """Presta un libro si hay copias disponibles."""
        encontrado = False
        for libro in self.libros:
            if libro.titulo == titulo:
                encontrado = True
                if libro.copias > 0:
                    libro.copias -= 1
                    print(f"✅ Libro '{titulo}' prestado. Quedan {libro.copias} copias.")
                    return
                else:
                    print(f"❌ No hay copias disponibles del libro '{titulo}'.")
                    return
        if not encontrado:
            print(f"❌ El libro '{titulo}' no se encuentra en la biblioteca.")
    def devolver_libro(self, titulo):
        """Devuelve un libro a la biblioteca."""
        encontrado = False
        for libro in self.libros:
            if libro.titulo == titulo:
                encontrado = True
                libro.copias += 1
                print(f"✅ Libro '{titulo}' devuelto. Ahora hay {libro.copias} copias.")
                return
        if not encontrado:
            print(f"❌ El libro '{titulo}' no pertenece a esta biblioteca.")
    def mostrar_libros(self):
        """Muestra el listado completo de libros en la biblioteca."""
        print("\n📚 Listado de libros en la biblioteca:")
        if not self.libros:
            print("La biblioteca está vacía.")
        for libro in self.libros:
            print(libro)