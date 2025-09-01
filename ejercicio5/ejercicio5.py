class Pelicula:
    def __init__(self,titulo,genero,año):
        self.titulo = titulo
        self.genero = genero
        self.año = año
        lista = []
        lista.append(self.titulo)
        lista.append(self.genero)
        lista.append(self.año)
        for a in lista:
            print(a)