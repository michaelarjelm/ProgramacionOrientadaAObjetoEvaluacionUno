# ejercicio5/Catalogo.py
class Catalogo:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def filtrar_por_genero(self, genero):
        for p in self.peliculas:
            if p.genero == genero:
                print(f"Título: {p.titulo}, Año: {p.ano}")

    def buscar_por_titulo(self, titulo):
        for p in self.peliculas:
            if p.titulo == titulo:
                print(f"Encontrado: {p.titulo}, Género: {p.genero}, Año: {p.ano}")
                return
        print("Película no encontrada.")

    def listar_todas(self):
        for p in self.peliculas:
            print(f"Título: {p.titulo}, Género: {p.genero}, Año: {p.ano}")