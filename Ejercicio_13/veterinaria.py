# Ejercicio 13 — Veterinaria y Mascotas 
# Crea una clase Mascota con nombre, especie y edad. Crea una clase Veterinaria que permita 
# registrar mascotas, buscar por nombre, listar todas y calcular la edad promedio de las mascotas. 

from mascota import Mascota

class Veterinaria:
    def __init__(self):
        self.mascotas = []

    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)
        print(f" Mascota '{mascota.nombre}' registrada.")

    def buscar_mascota(self, nombre):
        for m in self.mascotas:
            if m.nombre.lower() == nombre.lower():
                print(f"🔍 Mascota encontrada: {m}")
                return m
        print(f" No se encontró la mascota '{nombre}'.")
        return None

    def listar_mascotas(self):
        if not self.mascotas:
            print(" No hay mascotas registradas.")
        else:
            print("\n--- Mascotas registradas ---")
            for m in self.mascotas:
                print(m)

    def edad_promedio(self):
        if not self.mascotas:
            return 0
        promedio = sum(m.edad for m in self.mascotas) / len(self.mascotas)
        return promedio
