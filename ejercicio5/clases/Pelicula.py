# creamos la clase pelicula, estructura titulo, genero.año 
class Pelicula:
    def __init__(self, titulo: str, genero: str, año: int):
        self.titulo = titulo
        self.genero = genero
        self.año = año

    def __str__(self):
        return f"{self.titulo} ({self.año}) - Género: {self.genero}"
