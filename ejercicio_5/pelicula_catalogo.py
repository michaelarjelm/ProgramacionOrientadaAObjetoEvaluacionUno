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

