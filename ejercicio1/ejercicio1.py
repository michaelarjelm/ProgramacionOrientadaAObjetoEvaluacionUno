class Libro:
    def __init__(self,titulo,cantidad,copias):
        self.titulo = titulo
        self.cantidad = cantidad
        self.copias = copias
class Biblioteca:
    def __init__(self,agregar,prestar,devolver):
        self.agregar = []
        self.prestar = prestar
        self.devolver = devolver       
        self.agregar.append(agregar)
        self.agregar.remove(self.prestar)
        self.agregar.append(self.devolver)
    def mostrar (self):
        for libro in self.agregar:
            print(libro)
    
