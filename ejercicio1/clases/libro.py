#crear clase libro, titulo, autor, copias

class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

    def prestar(self):
        if self.copias > 0: 
            self.copias -= 1 
            return True  
        return False   

    def devolver(self):
        self.copias += 1


