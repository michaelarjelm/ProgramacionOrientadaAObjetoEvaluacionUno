# Ejercicio 7 — Agenda y Contacto 
# Crea una clase Contacto con nombre, teléfono y correo. Crea una clase Agenda que permita 
# agregar, buscar, eliminar y listar contactos. 

from contacto import Contacto

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        
        for c in self.contactos:
            if c.nombre.lower() == contacto.nombre.lower():
                print(f" El contacto '{contacto.nombre}' ya existe.")
                return
        self.contactos.append(contacto)
        print(f" Contacto '{contacto.nombre}' agregado.")

    def buscar_contacto(self, nombre):
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():
                print(f"🔍 Contacto encontrado: {c}")
                return c
        print(f" No se encontró el contacto '{nombre}'.")
        return None

    def eliminar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            self.contactos.remove(contacto)
            print(f" Contacto '{nombre}' eliminado.")

    def listar_contactos(self):
        if not self.contactos:
            print(" No hay contactos en la agenda.")
        else:
            print("\n--- Contactos en la Agenda ---")
            for c in self.contactos:
                print(c)
