#Crea una clase Mascota con nombre, especie y edad. Crea una clase Veterinaria que permita
#registrar mascotas, buscar por nombre, listar todas y calcular la edad promedio de las mascota
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

class Veterinaria:
    def __init__(self):
       self.listaMascotas = {}
    def registrar (self, mascota: Mascota):
        
