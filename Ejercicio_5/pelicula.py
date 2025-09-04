class Pelicula:
    def __init__(self, titulo, genero, anio):
        self.titulo = titulo
        self.genero = genero
        self.anio = anio

    def __str__(self):
        return f"{self.titulo} ({self.anio}) - Género: {self.genero}"
