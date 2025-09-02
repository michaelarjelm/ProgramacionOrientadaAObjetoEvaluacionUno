#Clase Grupo
class Grupo:
    def __init__(self, titulo):
        self.titulo = titulo
        self.lista = []
        
    def agrega(self, persona):
        if persona not in self.lista:
            print(f"{persona} se añadio al grupo {self.titulo}")
        else:
            print(f"{persona} ya se encuentra en el grupo")
    
    def quita(self, persona):
        if persona in self.lista:
            self.lista.remove(persona)
            print(f"{persona} ha sido removido del grupo {self.titulo}")
        else:
            print(f"{persona} no se encuentra en el grupo")
    
    def mostrar(self):
        print(f"\nIntegrantes del grupo {self.titulo}:")
        if self.lista:
            for p in self.lista:
                print(f" - {p}")
        else:
            print("No posee integrantes")