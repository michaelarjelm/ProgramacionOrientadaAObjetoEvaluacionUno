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
        print(f"Contacto '{contacto.nombre}' agregado.")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto
        return None 

    def eliminar_contacto(self, nombre):
        contacto_a_eliminar = self.buscar_contacto(nombre)
        if contacto_a_eliminar:
            self.contactos.remove(contacto_a_eliminar)
            print(f"Contacto '{nombre}' eliminado con éxito.")
            return True
        else:
            print(f"Error: No se encontró el contacto.")
            return False

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
            return
        
        for contacto in self.contactos:
            print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Correo: {contacto.correo}")

