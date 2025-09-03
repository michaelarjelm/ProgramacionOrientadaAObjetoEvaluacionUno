# hacemos el llamado con el import de contacto a la agenda 


from ejercicio7.clases.Contacto import Contacto
# creamos la clase agenda 
class Agenda:
    def __init__(self):
        self.contactos = []
# definimos agregar / nombre, telefono, correo 

    def agregar(self, nombre: str, telefono: str, correo: str) -> bool:
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():    # a qui se crea el contacto, y si ya existe pasa a la siguiente funcion 
                return False  # Ya existe
        nuevo = Contacto(nombre, telefono, correo)
        self.contactos.append(nuevo)
        return True
# definimos buscar contacto dentro de la lista 
    def buscar(self, nombre: str):
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():
                return c
        return None

    def eliminar(self, nombre: str) -> bool:
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():
                self.contactos.remove(c)
                return True
        return False

    def listar(self):
        return self.contactos
