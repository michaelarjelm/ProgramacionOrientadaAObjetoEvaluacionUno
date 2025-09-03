#Ejercicio 5 — Película y Catálogo
#Crea una clase película con título, género y año. 
#Crea una clase Catalogo que permita agregar películas, filtrar por género, buscar por título y listar todas.

class Pelicula:
    def __init__(self, titulo, genero, año):
        self.titulo = titulo
        self.genero = genero
        self.año = año

class Catalogo:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def filtrar_por_genero(self, genero):
        return [pelicula for pelicula in self.peliculas if pelicula.genero == genero]

    def buscar_por_titulo(self, titulo):
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                return pelicula
        return None

    def listar_todas(self):
        for pelicula in self.peliculas:
            print(f"Título: {pelicula.titulo}, Género: {pelicula.genero}, Año: {pelicula.año}")
