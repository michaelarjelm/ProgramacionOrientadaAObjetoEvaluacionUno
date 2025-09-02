#Creamos la agenda

class Contacto:
    def __init__(self, nombre, ntelefono, correo):
        self.nombre = nombre
        self.ntelefono = ntelefono
        self.correo = correo
        
        
        
class Agenda:
    def __init__(self):
        self.contactos = []
    
    def anadir_contacto(self, contacto):
        self.contactos.append(contacto)
        print(f'Contacto "{contacto.nombre}" agregado a la agenda.')
    
    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print('---- Contacto encontrado ----')
                print(f'Nombre: "{contacto.nombre}".')
                print(f'Telefono: "{contacto.ntelefono}".')
                print(f'Correo: "{contacto.correo}".')
                return contacto
        print(f'Contacto "{nombre}" encontrado en agenda.')
        return None
    
    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                print(f'"{contacto.nombre}" eliminado correctamente de la agenda.')
                return True
        print(f'El contacto "{nombre}" no existe, no se puede elimanar.')
        
    def lista_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
            return

        print("---- Lista de contactos ----")
        for contacto in self.contactos:
            print(f"Nombre: '{contacto.nombre}' | Teléfono: '{contacto.ntelefono}' | Correo: '{contacto.correo}'.")