# Ejercicio 5 — Película y Catálogo 
# Crea una clase película con título, género y año. Crea una clase Catalogo que permita agregar 
# películas, filtrar por género, buscar por título y listar todas. 

from pelicula import Pelicula

class Catalogo:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)
        print(f" Película agregada: {pelicula.titulo}")

    def filtrar_por_genero(self, genero):
        filtradas = [p for p in self.peliculas if p.genero.lower() == genero.lower()]
        if not filtradas:
            print(f" No se encontraron películas del género {genero}.")
        else:
            print(f"\n--- Películas del género {genero} ---")
            for p in filtradas:
                print(p)

    def buscar_por_titulo(self, titulo):
        for p in self.peliculas:
            if p.titulo.lower() == titulo.lower():
                print(f" Película encontrada: {p}")
                return
        print(f" No se encontró la película con título '{titulo}'.")

    def listar_todas(self):
        if not self.peliculas:
            print(" No hay películas en el catálogo.")
        else:
            print("\n--- Catálogo de Películas ---")
            for p in self.peliculas:
                print(p)
