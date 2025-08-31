#Construimos la clase Libro

class Libro:
    def __init__ (self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = int(copias)

    def consultar(self):
        print(f"'{self.titulo}', {self.autor}. Número de copias disponibles: {self.copias}.")

#Construimos la clase Biblioteca

class Biblioteca:
    def __init__(self,libro:Libro):
        self.listado = []

    def agregarLibro(self, libro:Libro):
        self.listado.append(libro)
        print(f"¡Has agregado '{libro}' a tu biblioteca!")
        
    
    def prestarLibro(self, libro:Libro):
        for libro in self.listado:
            if libro.copias >= 1:
                # libro.copias -1
                print(f"Has retirado {libro.titulo}")
            else:
                 print("No existen copias disponibles para retirar :(") 