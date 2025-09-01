class Agenda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contactos = []
    
    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print(f"\n'{contacto.nombre}' agregado a la agenda.")

    def buscar_contacto(self, contacto):
        if self.contactos:
            if contacto in self.contactos:
                print("\n-- Resultado de la busqueda:\n")
                print(contacto)
            else:
                print(f"\n-- Contacto '{contacto.nombre}' no encontrado --")
        else:
            print("\nLa agenda esta vacia!")

    def eliminar_contacto(self, contacto):
        if self.contactos:
            if contacto in self.contactos:
                self.contactos.remove(contacto)
                print(f"\n-- Se removio a '{contacto.nombre}' de tu agenda --")
            else:
                print(f"\n-- Contacto '{contacto.nombre}' no encontrado --")
        else:
            print("\nLa agenda esta vacia!")

    def listar_contactos(self):
        if self.contactos:
            print("\n--- Lista de contactos ---\n")
            for contacto in self.contactos:
                print(f"* Nombre: {contacto.nombre:10} | Telefono: {contacto.telefono:10} | Correo: {contacto.correo}")
        else:
            print("\nLa agenda esta vacia!")
