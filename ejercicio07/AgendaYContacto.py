# ~ Clase Contacto
class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}"

# ~ Clase Agenda para gestionar contactos

class Agenda:
    def __init__(self):
        self.contactos = [] # ~ Lista para almacenar los contactos

    def buscarContacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto
        return None
        print("Contacto no encontrado!")

    def agregarContacto(self, contacto):
        self.contactos.append(contacto)

    def eliminarContacto(self, nombre):
        contacto = self.buscarContacto(nombre) # ~ Buscar el contacto por nombre
        if contacto:
            self.contactos.remove(contacto)
            return True
        return False # ~ Retorna False si no se encontró el contacto

    def mostrarContactos(self):
        for contacto in self.contactos:
            print(contacto)

    
