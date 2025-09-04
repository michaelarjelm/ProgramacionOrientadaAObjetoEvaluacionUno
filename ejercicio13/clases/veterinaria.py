#Crea una clase Veterinaria que permita 
# registrar mascotas, buscar por nombre, listar todas y calcular la edad promedio de las mascotas. 
class Veterinaria:
    def __init__(self):
        self.mascotas = []

    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def buscar_por_nombre(self, nombre):
        for mascota in self.mascotas:
            if mascota.nombre == nombre:
                return mascota
        return None

    def listar_todas(self):
        for mascota in self.mascotas:
            print(f"Nombre: {mascota.nombre}, Especie: {mascota.especie}, Edad: {mascota.edad} años")

    def calcular_edad_promedio(self):
        if not self.mascotas:
            return 0
        total_edad = sum(mascota.edad for mascota in self.mascotas)
        return total_edad / len(self.mascotas)
    