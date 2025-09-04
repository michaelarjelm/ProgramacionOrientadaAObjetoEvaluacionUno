class Catalogo:
    def __init__(self):
        self.peliculas = []  

    def agregar(self, pelicula):
        self.peliculas.append(pelicula)
        print(f"Se agregó la película: {pelicula.titulo}")

    def listar(self):
        if not self.peliculas:
            print("No hay nada en el catalogo.")
        else:
            print("#Catálogo de películas#")
            for p in self.peliculas:
                print(p)

    def buscar_por_titulo(self, titulo):
        for p in self.peliculas:
            if p.titulo.lower() == titulo.lower():   
                return p
        return None

    def filtrar_por_genero(self, genero):
        resultado = []
        for p in self.peliculas:
            if p.genero.lower() == genero.lower():
                resultado.append(p)
        return resultado


