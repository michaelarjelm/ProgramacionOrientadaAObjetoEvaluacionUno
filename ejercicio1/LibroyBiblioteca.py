# Construccion clase libro:
class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = int(copias)

    def Preguntar(self):
        return (f'{self.titulo}, {self.autor}. Cantidad disponible: {self.copias}.')

# Construccion clase biblioteca:
class Biblioteca:
    def __init__(self):
        self.libros = []
        
    def Insertar(self, libro):
        self.libros.append(libro)
        print(f"¡Has agregado '{libro.titulo}' a tu biblioteca! Tienes {libro.copias} copias disponibles.")
        
    def Prestar(self, libro):
        if libro in self.libros:
            if libro.copias >= 1:
                libro.copias -= 1
                print(f'El libro prestado es: {libro.titulo}')
            else:
                print(f'¡No tenemos copias disponibles del libro: {libro.titulo}!')
        else:
            print(f'El libro "{libro.titulo}" no está en nuestra biblioteca.')        

    def Devolucion(self, libro):
        if libro in self.libros:
            libro.copias += 1
            print(f'Has hecho la devolucion: "{libro.titulo}" a la Biblioteca')
        else:
            print('Este libro no pertenece a nuestra biblioteca.')
            
    def VisualizarDisponibilidad(self):
        print("Lista disponible de libros en la Biblioteca:")
        for libro in self.libros:
            print(libro.Preguntar())
            