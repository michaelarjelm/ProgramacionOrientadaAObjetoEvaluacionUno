#Crea una clase Agenda que permita  agregar, buscar, eliminar y listar contactos.
from .contacto import Contacto  
class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print(f"Contacto '{contacto.nombre}' agregado a la agenda.")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto
        print(f"Contacto '{nombre}' no encontrado, ¿estas seguro que lo registraste?.")
        return None

    def eliminar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            self.contactos.remove(contacto)
            print(f"Contacto '{nombre}' eliminado de la agenda.")

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
            return
        print("Contactos en la agenda:")
        for contacto in self.contactos:
            print(contacto) 