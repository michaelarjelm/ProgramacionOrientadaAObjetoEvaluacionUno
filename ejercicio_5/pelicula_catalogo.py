##Crea una clase película con título, género y año.
##Crea una clase Catalogo que permita agregar películas, filtrar por género, buscar por título y listar todas.


class Pelicula:
    def __init__(self, titulo, genero, año):
        self.titulo = titulo
        self.genero = genero
        self.año = año 
    def __str__(self):
        return f"{self.titulo} ({self.año}) - Género: {self.genero}"

class Catalogo:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def listar_todas(self):
        if not self.peliculas:
            print("El catálogo está vacío.")
        else:
            for p in self.peliculas:
                print(p)

    def buscar_por_titulo(self, titulo):
        resultados = [p for p in self.peliculas if p.titulo.lower() == titulo.lower()]
        return resultados

    def filtrar_por_genero(self, genero):
        resultados = [p for p in self.peliculas if p.genero.lower() == genero.lower()]
        return resultados

pelicula1 = Pelicula("Matrix", "Ciencia Ficción", 1999)
pelicula2 = Pelicula("El Padrino", "Drama", 1972)
pelicula3 = Pelicula("Toy Story", "Animación", 1995)

catalogo = Catalogo()
catalogo.agregar_pelicula(pelicula1)
catalogo.agregar_pelicula(pelicula2)
catalogo.agregar_pelicula(pelicula3)

print("📋 Todas las películas:")
catalogo.listar_todas()

print("\n🔎 Buscar por título 'Matrix':")
for p in catalogo.buscar_por_titulo("Matrix"):
    print(p)

print("\n🎬 Filtrar por género 'Drama':")
for p in catalogo.filtrar_por_genero("Drama"):
    print(p)