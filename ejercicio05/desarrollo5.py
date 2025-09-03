# Clase pelicula

class Pelicula:
    def __init__(self, titulo, genero, año):
        self.titulo = titulo
        self.genero = genero
        self.año = año

#clase catalogo

class Catalogo:
    def __init__(self):
        self.peliculas = []

#Sumamos peliculas

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def listar_todas(self):
        if not self.peliculas:
            print("El catalogo esta vacio.")
            return

        print("Listado completo de peliculas")
        for peli in self.peliculas:
            print(f"Titulo: {peli.titulo}, Genero: {peli.genero}, Año: {peli.año}")

    def buscar_por_titulo(self, titulo):
        resultados = []
        for peli in self.peliculas:
            if titulo.lower() in peli.titulo.lower():
                resultados.append(peli)
        return resultados

    def filtrar_por_genero(self, genero):
        resultados = []
        for peli in self.peliculas:
            if peli.genero.lower() == genero.lower():
                resultados.append(peli)
        return resultados