#Clase Catalogo
class Catalogo:
    def __init__(self):
        self.peliculas = []
    
    def agrega_pelicula(self, pelicula):
        self.peliculas.append(pelicula)
        
    def filtrar_genero(self, genero):
        resultado = []
        for peli in self.peliculas:
            if peli.genero == genero:
                resultado.append(peli)
        return resultado
    
    def buscar_titulo(self, titulo):
        for peli in self.peliculas:
            if peli.titulo == titulo:
                return peli
        return None
    
    def lista_completa(self):
        for peli in self.peliculas:
            print(f"{peli.titulo} - {peli.genero} - {peli.año}")    