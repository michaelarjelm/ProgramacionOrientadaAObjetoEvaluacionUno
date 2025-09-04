class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def buscar_contacto(self, nombre):
        for c in self.contactos: #buscar en la lista de contactos
            if c.nombre == nombre:
                print(f"Encontrado: {c.nombre}, Tel: {c.telefono}, Correo: {c.correo}")
                return
        print("Contacto no encontrado.")

    def eliminar_contacto(self, nombre):
        for c in self.contactos: 
            if c.nombre == nombre:
                self.contactos.remove(c) #para eliminar
                print(f"Eliminado: {nombre}")
                return
        print("Contacto no encontrado.")

    def listar_contactos(self):
        for c in self.contactos:
            print(f"Nombre: {c.nombre}, Tel: {c.telefono}, Correo: {c.correo}")