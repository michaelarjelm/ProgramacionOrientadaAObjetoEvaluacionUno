class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        
        
    def presta_libro(self,titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                if libro.copias > 0:
                    libro.copias -= 1
                    return True
                else:
                    return False
        return None
        
        
    def devolver_libro(self,titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                libro.copias +=1
                return True
        return None
            
        
    def mostrar_lista_libros(self):
        if self.libros:
            for libro in self.libros:
                print(f"título: {libro.titulo} - autor: {libro.autor} - copias: {libro.copias}")
        else:
            print("No hay libros en la biblioteca")