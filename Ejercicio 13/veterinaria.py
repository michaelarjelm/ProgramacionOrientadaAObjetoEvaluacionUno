from mascota import Mascota

class Veterinaria:
    def __init__(self):
        self.mascotas = []

    def registrar_mascota(self, nombre, especie, edad):
        nueva_mascota = Mascota(nombre, especie, edad)
        self.mascotas.append(nueva_mascota)
        print(f"Mascota '{nombre}' registrada.")

    def buscar_por_nombre(self, nombre):
        for mascota in self.mascotas:
            if mascota.nombre.lower() == nombre.lower():
                return mascota
        return None

    def listar_mascotas(self):
        if not self.mascotas:
            print("No hay mascotas registradas.")
            return
        print("Mascotas registradas:")
        for mascota in self.mascotas:
            print(mascota)

    def calcular_edad_promedio(self):
        if not self.mascotas:
            print("No hay mascotas para calcular la edad promedio.")
            return 0
        total_edad = sum(mascota.edad for mascota in self.mascotas)
        return total_edad / len(self.mascotas)
