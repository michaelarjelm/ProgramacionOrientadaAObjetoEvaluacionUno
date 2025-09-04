#Crea una clase Catalogo que permita agregar películas, filtrar por género, buscar por título y listar todas.
from .pelicula import Pelicula

class Catalogo:
    def __init__(self):
        self.peliculas: list[Pelicula] = []

    def agregar_pelicula(self, pelicula: Pelicula) -> None:
        self.peliculas.append(pelicula)
        print(f'Película "{pelicula.titulo}" agregada al catálogo.')

    def filtrar_por_genero(self, genero: str) -> list[Pelicula]:
        return [p for p in self.peliculas if p.genero.lower() == genero.lower()]

    def buscar_por_titulo(self, titulo: str) -> Pelicula | None:
        for p in self.peliculas:
            if p.titulo.lower() == titulo.lower():
                return p
        print(f'No se encontró la película con título "{titulo}".')
        return None

    def listar_todas(self) -> list[Pelicula]:
        return self.peliculas
    