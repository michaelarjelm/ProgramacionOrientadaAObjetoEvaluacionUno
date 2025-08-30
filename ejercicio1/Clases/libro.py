class Libro:
    def __init__(self,titulo,autor,copias):
        self.titulo=titulo
        self.autor=autor
        self.copias=copias

    def libro(self):
        return f"{self.titulo} de {self.autor} con {self.copias} copias"
    