from Ejercicio7.Contacto import Contacto


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar(self, nombre, telefono, correo):
        # Evitar duplicados por nombre
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():
                return False
        self.contactos.append(Contacto(nombre, telefono, correo))
        return True

    def buscar(self, nombre):
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():
                return c
        return None

    def eliminar(self, nombre):
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():
                self.contactos.remove(c)
                return True
        return False

    def listar(self):
        return self.contactos 