class Pelicula:
    def __init__(self, titulo, genero, anio):
        self.titulo = titulo
        self.genero = genero
        self.anio = anio

    def __str__(self):
        return f"Película: {self.titulo} ({self.anio}) - Género: {self.genero}"

class Catalogo:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, pelicula):
        if isinstance(pelicula, Pelicula):
            self.peliculas.append(pelicula)
            print(f"Película '{pelicula.titulo}' agregada al catálogo")
        else:
            print("Error: Solo se pueden agregar objetos de tipo Pelicula")

    def listar_peliculas(self):
        if not self.peliculas:
            print("El catálogo está vacío")
            return
        print("\n--- Catálogo de Películas ---")
        for pelicula in self.peliculas:
            print(pelicula)
        print("-----------------------------")

    def buscar_por_titulo(self, titulo):
        resultados = []
        for pelicula in self.peliculas:
            if titulo.lower() in pelicula.titulo.lower():
                resultados.append(pelicula)
        return resultados

    def filtrar_por_genero(self, genero):
        resultados = []
        for pelicula in self.peliculas:
            if pelicula.genero.lower() == genero.lower():
                resultados.append(pelicula)
        return resultados



#Crear películas
predator = Pelicula("Depredador", "Ciencia Ficción", 1987)
terminator = Pelicula("Terminator 2", "Ciencia Ficción", 1991)
gladiador = Pelicula("Gladiador", "Acción", 2000)
pulp_fiction = Pelicula("Pulp Fiction", "Crimen", 1994)

#Crear un catálogo
mi_catalogo = Catalogo()

#Agregar películas al catálogo
mi_catalogo.agregar_pelicula(predator)
mi_catalogo.agregar_pelicula(terminator)
mi_catalogo.agregar_pelicula(gladiador)
mi_catalogo.agregar_pelicula(pulp_fiction)

#Listar todas las películas
mi_catalogo.listar_peliculas()

#Buscar películas por título
print("\n--- Buscando películas con 'Terminator' ---")
resultados_titulo = mi_catalogo.buscar_por_titulo("Terminator")
if resultados_titulo:
    for p in resultados_titulo:
        print(p)
else:
    print("No se encontraron películas con ese título.")

#Filtrar películas por género
print("\n--- Filtrando películas de Ciencia Ficción ---")
resultados_genero = mi_catalogo.filtrar_por_genero("Ciencia Ficción")
if resultados_genero:
    for p in resultados_genero:
        print(p)
else:
    print("No se encontraron películas de ese género.")
