class Catalogo:
    def __init__(self):
        self.peliculas = []

    def agregar(self, pelicula):
        self.peliculas.append(pelicula)

    def listar(self):
        return self.peliculas

    def buscar_por_titulo(self, titulo):
        for p in self.peliculas:
            if p.titulo.lower() == titulo.lower():
                return p
        return None

    def filtrar_por_genero(self, genero):
        return [p for p in self.peliculas if p.genero.lower() == genero.lower()]   