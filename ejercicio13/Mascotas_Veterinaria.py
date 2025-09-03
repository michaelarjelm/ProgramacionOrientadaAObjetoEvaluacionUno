#Ejercicio 13 — Veterinaria y Mascotas
#Crea una clase Mascota con nombre, especie y edad.
#Crea una clase Veterinaria que permita registrar mascotas, buscar por nombre, listar todas y calcular la edad promedio de las mascotas.

class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

class Veterinaria:
    def __init__(self):
        self.mascotas = []

    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def buscar_mascota(self, nombre):
        for mascota in self.mascotas:
            if mascota.nombre == nombre:
                return mascota
        return None

    def listar_mascotas(self):
        for mascota in self.mascotas:
            print(f"Nombre: {mascota.nombre}, Especie: {mascota.especie}, Edad: {mascota.edad}")

    def calcular_edad_promedio(self):
        if not self.mascotas:
            return 0
        total_edad = sum(mascota.edad for mascota in self.mascotas)
        return total_edad / len(self.mascotas)
