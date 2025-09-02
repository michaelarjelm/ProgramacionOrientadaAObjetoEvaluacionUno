# Crea una clase Contacto con nombre, teléfono y correo. Crea una clase Agenda que permita agregar, buscar, eliminar y listar contactos.

class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar(self, contacto: Contacto):
        self.contactos[contacto.nombre.lower()] = contacto
        print(f"Has agregado al contacto: {contacto.nombre}")

    def buscar(self, nombre):
        return self.contactos.get(nombre.lower())

    def eliminar(self, nombre):
        if nombre.lower() in self.contactos:
            del self.contactos[nombre.lower()]
            print(f"Has eliminado al contacto: {nombre} de tu agenda")
        else:
            print(f"Contacto {nombre} no encontrado en tu agenda")

    def listar(self):
        for contacto in self.contactos.values():
            print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Correo: {contacto.correo}")