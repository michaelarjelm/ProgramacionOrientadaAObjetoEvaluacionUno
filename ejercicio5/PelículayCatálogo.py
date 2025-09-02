#Creamoas las peliculas
class Pelicula:
    def __init__(self, titulo, genero, año_estreno):
        self.titulo = titulo
        self.genero = genero
        self.año_estreno = año_estreno
    
#Creamos el catalogo de peliculas
class Catalogo:
    def __init__(self):
        self.peliculas = []
    
    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)
        print(f"Pelicula '{pelicula.titulo}' agregada.")
        
    def fintro_por_genero(self, genero):
        peliculas_filtradas = []
        for pelicula in self.peliculas:
            if pelicula.genero.lower() == genero.lower():
                peliculas_filtradas.append(pelicula)
    
        if not peliculas_filtradas:
            print(f'No hay peliculas del genero "{genero}".')
            return []
        
        print(f'------Pelicula del genero "{genero}"------')
        for pelicula in peliculas_filtradas:
            print(f"Titulo: '{pelicula.titulo}' - Año de estreno '{pelicula.año_estreno}'.")
        return peliculas_filtradas
    
    def buscar_pelicula(self, titulo):
        for pelicula in self.peliculas:
            if pelicula.titulo.lower() == titulo.lower():
                print(f'Pelicula encontrada: "{pelicula.titulo}".')
                return pelicula
        print(f'No se econtro la pelicula "{titulo}" que buscabas.')
        return None
    
    def listado_peliculas(self):
        if not self.peliculas:
            print('El catlogo no contiene peliculas.')
            return
        print('--------Lista de peliculas disponibles-------')
        for pelicula in self.peliculas:
            print(f'Titulo: "{pelicula.titulo}" - Genero: "{pelicula.genero}".')