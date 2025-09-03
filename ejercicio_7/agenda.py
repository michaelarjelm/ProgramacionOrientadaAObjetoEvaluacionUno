class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Correo: {self.correo}"


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print(f"Contacto {contacto.nombre} agregado.")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto
        return None

    def eliminar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            self.contactos.remove(contacto)
            print(f"Contacto {nombre} eliminado.")
        else:
            print(f"Contacto {nombre} no encontrado.")

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            for contacto in self.contactos:
                print(contacto)
