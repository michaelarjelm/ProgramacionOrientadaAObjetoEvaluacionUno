class Catalogo:
    def __init__(self):
        self.catalogo = []

    def agregar_pelicula(self, nombre_pelicula):
        self.catalogo.append(nombre_pelicula)

    def filtrar_por_genero(self, genero):
        if self.catalogo:
            peliculas_filtradas = []
            for pelicula in self.catalogo:
                if genero == pelicula.genero:
                    peliculas_filtradas.append(pelicula)
            if peliculas_filtradas:
                print(f"\n--- {genero.upper()} ---")
                print(f"Peliculas disponibles ({len(peliculas_filtradas)})\n")
                for pelicula in peliculas_filtradas:
                    print(f"* {pelicula.titulo} ({pelicula.año})")
            else:
                print(f"\nNo hay peliculas en el genero {genero.upper()}")
        else:
            print("\n-- El catalogo esta vacio --")

    def buscar_por_titulo(self, titulo):
        if self.catalogo:
            resultado_busqueda = []
            for pelicula in self.catalogo:
                if titulo == pelicula.titulo:
                    resultado_busqueda.append(pelicula.titulo)
                    resultado_busqueda.append(pelicula.año)
                    resultado_busqueda.append(pelicula.genero)
            if resultado_busqueda:
                print("\n*** Resultado de la busqueda ***\n")
                print(f"* Titulo: {resultado_busqueda[0]}\n* Año: {resultado_busqueda[1]}\n* Genero: {resultado_busqueda[2]}")
            else:
                print("\n-- Pelicula no encontrada --")
        else:
            print("-- Catalogo vacio --")

    def listar_peliculas(self):
        print("\n--- Catalogo de peliculas ---\n")
        for pelicula in self.catalogo:
            print(f"* {pelicula}")

