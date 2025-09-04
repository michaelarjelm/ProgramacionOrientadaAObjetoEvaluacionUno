class Pelicula:
    def __init__(self, titulo, genero, año):
        self.titulo = titulo
        self.genero = genero
        self.año = año

    def __str__(self):
        return f"{self.titulo} ({self.año}) - Género: {self.genero}"
