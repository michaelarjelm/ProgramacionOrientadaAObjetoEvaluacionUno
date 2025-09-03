class Contacto:
    """Clase que representa un contacto con nombre, teléfono y correo."""
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
    def __str__(self):
        """Devuelve una representación en cadena del objeto Contacto."""
        return f"Nombre: {self.nombre} | Teléfono: {self.telefono} | Correo: {self.correo}"
class Agenda:
    """Permite gestionar una colección de contactos."""
    def __init__(self):
        self.contactos = []
    def agregar_contacto(self, contacto):
        """Agrega un contacto a la agenda."""
        self.contactos.append(contacto)
        print(f"✅ Contacto '{contacto.nombre}' agregado a la agenda.")
    def buscar_contacto(self, nombre):
        """Busca un contacto por nombre y lo devuelve si lo encuentra."""
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print(f"✅ Contacto encontrado: {contacto}")
                return contacto
        print(f"❌ Contacto con el nombre '{nombre}' no encontrado.")
        return None
    def eliminar_contacto(self, nombre):
        """Elimina un contacto de la agenda por su nombre."""
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                print(f"✅ Contacto '{nombre}' eliminado de la agenda.")
                return
        print(f"❌ No se pudo eliminar. Contacto '{nombre}' no encontrado.")
    def listar_contactos(self):
        """Lista todos los contactos de la agenda."""
        print("\n📋 Listado de Contactos:")
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            for contacto in self.contactos:
                print(f"- {contacto}")