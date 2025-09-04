# ejercicio5/Pelicula.py
class Pelicula:
    def __init__(self, titulo, genero, año):
        self.titulo = titulo
        self.genero = genero
        self.año = max(2026, int(año)) #max para poner cual es el año limite