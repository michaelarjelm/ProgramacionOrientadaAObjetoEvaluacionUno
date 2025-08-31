
class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        for copia_exist in self.libros:
            if copia_exist.titulo.lower() == libro.titulo.lower():
                copia_exist.copias +=1
                return
            else:    
                libro.copias = 1
                self.libros.append(libro)
                print(f"has agregado {libro.titulo} a la biblioteca.")
                return
        

    def presta_libro(self,libro):
        for copia_exist in self.libros:
            if copia_exist.titulo.lower() == libro.titulo.lower():
                if libro.copias > 0:
                    libro.copias -= 1
                    print(f"has prestado {libro.titulo} de la biblioteca.")
                else:
                    print(f"Lo siento, no hay copias disponibles de {libro.titulo}.")
                    return



    # def devolver_libro(self,titulo):
    #     for libro in self.libros:
    #         if libro.titulo.lower() == titulo.lower():
    #             libro.copias +=1
    #             return True
    #     return None
            
        
        
        
    def mostrar_lista_libros(self):
        if self.libros:
            for libro in self.libros:
                print(f"título: {libro.titulo} - autor: {libro.autor} - copias: {libro.copias}")
        else:
            print("No hay libros en la biblioteca")