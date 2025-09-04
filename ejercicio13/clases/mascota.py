# Crea una clase Mascota con nombre, especie y edad
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        print(f"Mascota creada: {self.nombre}, Especie: {self.especie}, Edad: {self.edad} años")
        