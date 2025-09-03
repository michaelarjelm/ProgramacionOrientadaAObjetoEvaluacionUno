#Ejercicio 7 — Agenda y Contacto
# Crea una clase Contacto con nombre, teléfono y correo. Crea una clase Agenda que permita
# agregar, buscar, eliminar y listar contactos.
from ejercicio7.clases import contacto


class Agenda:
    def __init__(self):
        self.agenda = []

    def agregar_contacto(self, nombre, apellido, telefono, correo):
        nuevo_contacto = contacto.Contacto(nombre, apellido, telefono, correo)
        self.agenda.append(nuevo_contacto)
        
    def buscar_contacto(self):
        nombre = input("Buscar contacto: ")
        for contacto in self.agenda:
            if contacto.nombre.lower() == nombre.lower() or contacto.apellido.lower() == nombre.lower():
                print(f"{contacto.nombre} {contacto.apellido}, Teléfono: {contacto.telefono}, Correo: {contacto.correo}")
                return contacto
            else:
                print("No se encontró el contacto")
                return 

    def eliminar_contacto(self):
        
        contacto_a_eliminar = self.buscar_contacto()

        if contacto_a_eliminar:
            confirmacion = input(f"¿deseas eliminar a {contacto_a_eliminar.nombre}? (si/no): ")
            if confirmacion.lower() == 'si':
                self.agenda.remove(contacto_a_eliminar)
                print(f"Contacto '{contacto_a_eliminar.nombre}' eliminado exitosamente.")
            elif confirmacion.lower() == 'no':
                print("Eliminación cancelada.")
                return None

    def listar_contactos(self):
        for contacto in self.agenda:
            print(contacto)