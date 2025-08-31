#Crea una clase película con título, género y año. Crea una clase Catalogo que permita agregar películas, filtrar por género, buscar por título y listar toda
class Pelicula:
    def __init__(self, titulo, genero, año):
        self.titulo = titulo
        self.genero = genero
        self.año = año

class Catalogo:
    def __init__(self):
        self.listadoPelicula = {}

    def agregar (self, pelicula: Pelicula):
        self.listadoPelicula[pelicula.titulo] = pelicula
        print (f"Se agregó: {pelicula.titulo}a tu catálogo")

    def filtrar(self, pelicula: Pelicula, genero):
        for pelicula in self.listadoPelicula.values():
            if pelicula.genero.lower() == genero.lower():
                print (f"Película '{pelicula.titulo}' encontrada en género: {pelicula.genero}")
            else:
                print (f"Película no encontrada bajo ningún filtro")
        return (f"No se encontró la película")

    #def buscar (self):
    
    #def listar (self):