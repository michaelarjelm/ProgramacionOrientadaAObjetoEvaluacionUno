#Clase Libro
class Libro:
    def __init__(self, titulo, autor, ndecopias ):
        self.titulo = titulo
        self.autor = autor
        self.ndecopias = ndecopias
    
    def mostrar_info(self):
        return f"El libro es {self.titulo} fue escrito por {self.autor} y el numero de copias disponibles son {self.copias}"
