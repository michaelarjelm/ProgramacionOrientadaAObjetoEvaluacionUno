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
        self.listaMascotas[mascota.nombre] = mascota
        print (f"Has registrado a la mascota: {mascota.nombre}, especie: {mascota.especie}, edad: {mascota.edad} años")
   
    def buscar (self, nombre):
        buscador = self.listaMascotas.get(nombre.lower())
        if buscador == nombre:
            print (f" Se ha encontrado la mascota: {nombre}, especie: {buscar.especie}, edad: {buscar.edad} años")
        else: 
            print| (f"No se encontró la mascota con el nombre: {nombre}")
    
    def listar (self):
        print ("Listado de todas las mascotas registradas:")
        for mascota in self.listaMascotas.values():
            print (f"Nombre: {mascota.nombre}, Especie: {mascota.especie}, Edad: {mascota.edad} años")
    
    def edadPromedio (self):
        totalEdad = sum(mascota.edad for mascota in self.listaMascotas.values())
        return totalEdad / len(self.listaMascotas)
    
    
