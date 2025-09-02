# ~ Ejercicio 5: Película y Catálogo
# Crea una clase Pelicula con atributos título, género y año de lanzamiento. Luego, crea una clase Catalogo que pueda almacenar múltiples objetos Pelicula. Implementa métodos para agregar películas al catálogo, listar todas las películas y buscar películas por género o título.

class Pelicula:
    def __init__(self, titulo, genero, anio):
        self.titulo = titulo
        self.genero = genero
        self.anio = anio

    def consultarPelicula(self):
        return f"{self.titulo} ({self.anio}). Género: {self.genero}"
    
class Catalogo:
    def __init__(self):
        self.peliculas = [] # ~ Lista para almacenar objetos Pelicula

    def agregarPeliculas(self, pelicula: Pelicula): 
        self.peliculas.append(pelicula)
        print(f"Agregaste '{pelicula.titulo}' al catálogo.")

    def listarPeliculas(self): # ~ Listar todas las películas en el catálogo
        if not self.peliculas:
            print("El catálogo está vacío")
        else:
            print("Blockbuster:") 
            for pelicula in self.peliculas:
                print(pelicula.consultarPelicula())
        
    def filtrarPorGenero(self, genero: str): # ~ Buscar películas por género
        peliculasEncontradas = [pelicula for pelicula in self.peliculas if pelicula.genero.lower() == genero.lower()]
        if not peliculasEncontradas:
            print(f"No se encontraron películas")
        else:
            print(f"Películas del género '{genero}':")
            for pelicula in peliculasEncontradas:
                print(pelicula.consultarPelicula())

    def buscarPorTitulo(self, titulo: str): # ~ Buscar una película por título
        for pelicula in self.peliculas:
            if pelicula.titulo.lower() == titulo.lower():
                return pelicula.consultarPelicula()
        return "No se encontró la película"
    