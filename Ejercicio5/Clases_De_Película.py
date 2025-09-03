class Pelicula:
    """Representa una película con título, género y año."""
    def __init__(self, titulo, genero, año):
        self.titulo = titulo
        self.genero = genero
        self.año = año
    def __str__(self):
        """Devuelve una representación en cadena del objeto Pelicula."""
        return f"'{self.titulo}' ({self.año}) - Género: {self.genero}"
class Catalogo:
    """Permite gestionar una colección de películas."""
    def __init__(self):
        self.peliculas = []
    def agregar_pelicula(self, pelicula):
        """Agrega una película al catálogo."""
        self.peliculas.append(pelicula)
        print(f"✅ Película '{pelicula.titulo}' agregada al catálogo.")
    def listar_todas(self):
        """Lista todas las películas del catálogo."""
        print("\n🎬 Listado de todas las películas:")
        if not self.peliculas:
            print("El catálogo está vacío.")
        else:
            for pelicula in self.peliculas:
                print(f"- {pelicula}")
    def buscar_por_titulo(self, titulo):
        """Busca una película por su título (sin distinguir mayúsculas y minúsculas)."""
        for pelicula in self.peliculas:
            if pelicula.titulo.lower() == titulo.lower():
                print(f"✅ Película encontrada: {pelicula}")
                return pelicula
        print(f"❌ No se encontró la película con el título '{titulo}'.")
        return None
    def filtrar_por_genero(self, genero):
        """Filtra y lista las películas por un género específico."""
        peliculas_encontradas = [
            p for p in self.peliculas if p.genero.lower() == genero.lower()
        ]
        print(f"\n🎬 Películas encontradas para el género '{genero}':")
        if not peliculas_encontradas:
            print("No se encontraron películas para este género.")
        else:
            for pelicula in peliculas_encontradas:
                print(f"- {pelicula}")
        return peliculas_encontradas