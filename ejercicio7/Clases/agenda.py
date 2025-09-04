
class Agenda:
    def __init__(self):
        self.contactos = []
        


    def agregar(self,contacto):
        self.contactos.append(contacto)
        print("Contacto agregado")
        print({contacto.nombre})
    

    def buscar(self,nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto
        return None
    
    def eliminar(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
            print(f"Contacto eliminado,{contacto}")
            return
    print("No se encontró el contacto")



    def listar(self):
        for contacto in self.contactos:
            print(f"Lista de contactos")
            print(contacto)



