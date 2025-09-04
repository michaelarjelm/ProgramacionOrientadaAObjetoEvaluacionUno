# Crea una clase película con título, género y año.

class Pelicula:
    def __init__(self, titulo: str, genero: str, año: int):
        self.titulo = titulo
        self.genero = genero
        self.anio = año  # Sin tilde en el atributo y sin que que suene grosero ajaja

    def __str__(self):
        return f"{self.titulo} ({self.anio}) - Género: {self.genero}"
    
