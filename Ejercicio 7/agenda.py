from contacto import Contacto

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, correo):
        nuevo_contacto = Contacto(nombre, telefono, correo)
        self.contactos.append(nuevo_contacto)
        print(f"Contacto '{nombre}' agregado.")

    def buscar_contacto(self, nombre):
        encontrados = [c for c in self.contactos if c.nombre.lower() == nombre.lower()]
        return encontrados

    def eliminar_contacto(self, nombre):
        contactos_a_eliminar = [c for c in self.contactos if c.nombre.lower() == nombre.lower()]
        if not contactos_a_eliminar:
            print(f"No se encontró contacto con el nombre '{nombre}'.")
            return False
        for contacto in contactos_a_eliminar:
            self.contactos.remove(contacto)
        print(f"Contacto(s) '{nombre}' eliminado(s).")
        return True

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
            return
        print("Contactos en la agenda:")
        for contacto in self.contactos:
            print(contacto)
