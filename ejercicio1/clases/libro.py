# Ejercicio 1 — Libro y Biblioteca 
# Crea una clase Libro con título, autor y cantidad de copias
class Libro:
    def __init__(self, titulo:str, autor:str, copias:int):
        self.titulo = titulo.upper()
        self.autor = autor.upper()
        self.copias = copias
       

    def __str__(self): 
        return f'Del libre: "{self.titulo}", cuyo autor es:"{self.autor}", tiene {self.copias} copias disponibles.'
    
    