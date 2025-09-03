# clase libro:

class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = int(copias)

    def preguntar(self):
        return (f'{self.titulo}, {self.autor}. Cantidad disponible: {self.copias}.')

# clase biblioteca:
    
class Biblioteca:
    def __init__(self):
        self.libros = []

#insertando libros:
         
    def InsertarLibro(self, libro):
        self.libros.append(libro)
        print (f"¡sumaste {libro.titulo} a tu solicitud!")

#prestando libros:

    def PrestarLibro(self, libro):
        for li in self.libros:
            if li.titulo == libro.titulo:
                if libro.copias >=1:
                    libro.copias -=1
                    print (f'El libro ha sido cargado {libro.titulo} con exito')
                    return
                else:
                    print('¡Lo sentimos, no tenemos copias disponible en este momento!')
                    return
        print('El libro no se encuentra disponible en la biblioteca.')
        return
    

    