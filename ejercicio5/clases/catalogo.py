class Catalogo:
    def __init__(self):
        self.catalogo = []
    
    def agregar_pelicula(self,pelicula):
            self.catalogo.append(pelicula)
            print(f"Se ha agregado {pelicula.titulo} al catálogo")
        
        
    def lista_catalogo(self):
            print("***catalogo disponible***: ")
            for pelicula in self.catalogo:
                print(f"{pelicula.titulo}, {pelicula.genero}, {pelicula.año}")
                
                
    def busqueda_titulo(self):
        while True:
            titulo_pelicula =input("Qué película deseas ver?: ").strip()
            for pelicula in self.catalogo:
                if f"{titulo_pelicula}".lower() == f"{pelicula.titulo}".lower():
                    print("título encontrado.¡disfruta de la película!")
                    return
            else:
                print("Lo sentimos, el título que buscas no se encuentra disponible.")
                
    
    
    def filtro_genero(self):
        while True:
            genero = input ("Buscar género: ")
            for pelicula in self.catalogo:
                if f"{pelicula.genero}".lower() == f"{genero}".lower():
                    print(pelicula.titulo)
                    return
            else:
                print("género ingresado no existe")
            