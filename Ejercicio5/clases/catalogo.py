class Catalogo:
    def __init__(self, nombre):
        self.nombre = nombre
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
            print("\nEl catalogo esta vacio")

    def buscar_por_titulo(self, pelicula):
        if self.catalogo:
            if pelicula in self.catalogo:
                print("\nResultado de la busqueda: \n")
                print(f"* Titulo: {pelicula.titulo} | Genero: {pelicula.genero} | Año: {pelicula.año}")
            else:
                print("Pelicula no encontrada")  

    def listar_peliculas(self):
        print("\n--- Catalogo de peliculas ---\n")
        for pelicula in self.catalogo:
            print(f"* {pelicula}")

