# creamos la clase catalogo 
from ejercicio5.clases.Pelicula import Pelicula

class Catalogo:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, pelicula: Pelicula):
        self.peliculas.append(pelicula)

    def listar(self):
        if not self.peliculas:
            print("Ups!! no hay películas en el catálogo.")
        else:
            print(" Catálogo de películas:")
            for peli in self.peliculas:
                print(" -", peli)

    def buscar_por_titulo(self, titulo: str):
        for peli in self.peliculas:
            if peli.titulo.lower() == titulo.lower():
                return peli
        return None

    def filtrar_por_genero(self, genero: str):
        return [peli for peli in self.peliculas if peli.genero.lower() == genero.lower()]
