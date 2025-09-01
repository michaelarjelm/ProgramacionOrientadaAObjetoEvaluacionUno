class Pelicula:
    def __init__(self, titulo, genero, año):
        self.titulo = titulo
        self.genero = genero
        self.año = año
    
    def __str__(self):
        return f"Titulo: {self.titulo:15} * Genero: {self.genero:16} * Año: {self.año}"