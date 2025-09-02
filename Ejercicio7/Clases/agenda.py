#Clase Agenda

from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio7.Clases.contacto import Contacto

class Agenda:
    def __init__(self):
        self.contactos = []
    
    def agrega_contacto(self, nombre, telefono, correo):
        contacto = Contacto(nombre, telefono, correo)
        self.contactos.append(contacto)
        print(f"El contacto {nombre} ha sido agregado")
    
    def busqueda_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto
        return None

    def elimina_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                self.contactos.remove(contacto)
                print(f"El contacto {nombre} ha sido eliminado")
                return
        print(f"El contacto {nombre} no ha sido encontrado")
    
    def listar_contactos(self):
        if not self.contactos:
            print("No hay contactos guardados")
        for contacto in self.contactos:
            print(f"Nombre: {contacto.nombre}, Telefono: {contacto.telefono}, Correo: {contacto.correo}")