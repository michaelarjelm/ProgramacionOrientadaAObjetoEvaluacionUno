##Crea una clase Contacto con nombre, teléfono y correo. 
##Crea una clase Agenda que permita agregar, buscar, eliminar y listar contactos.

class Contacto:
    def __init__(self,nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
    
class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def listar_contactos(self):
        for c in self.contactos:
            print(c.nombre, c.telefono, c.correo)

    def buscar_contacto(self, nombre):
        for c in self.contactos:
            if c.nombre == nombre:
                print(c.nombre, c.telefono, c.correo)
                return
        print("No se ha encontro el contacto.")

    def eliminar_contacto(self, nombre):
        for c in self.contactos:
            if c.nombre == nombre:
                self.contactos.remove(c)
                print("Contacto eliminado.")
                return
        print("No se ha encontrado el contacto.")



    

