##Crea una clase Mascota con nombre, especie y edad. 
##Crea una clase Veterinaria que permita registrar mascotas, buscar por nombre, 
##listar todas y calcular la edad promedio de las mascotas.

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
        print(f"Mascota {mascota.nombre} registrada.")

    def buscar_mascota(self, nombre):
        for m in self.mascotas:
            if m.nombre == nombre:
                print(f"Encontrada: {m.nombre} - {m.especie} - {m.edad} años")
                return
        print("No se encontró la mascota.")

    def listar_mascotas(self):
        for m in self.mascotas:
            print(f"{m.nombre} - {m.especie} - {m.edad} años")

    def edad_promedio(self):
        if not self.mascotas:
            return 0
        total = sum(m.edad for m in self.mascotas)
        return total / len(self.mascotas)
