
class Libro:
    def __init__(self,titulo,autor,copias):
            self.titulo = titulo
            self.autor = autor
            self.copias = copias


    def detalles_libro(self):
        return f"título: {self.titulo} - autor: {self.autor} - copias: {self.copias}"

