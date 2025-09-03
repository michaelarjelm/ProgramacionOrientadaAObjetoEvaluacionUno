#Ejercicio 7 — Agenda y Contacto
#Crea una clase Contacto con nombre, teléfono y correo. 
# Crea una clase Agenda que permita agregar, buscar, eliminar y listar contactos.

class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto
        return None

    def eliminar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            self.contactos.remove(contacto)
            return True
        return False

    def listar_contactos(self):
        return self.contactos
