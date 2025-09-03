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
        print(f"Mascota {mascota.nombre} registrada con éxito.")

    def buscar_mascota(self, nombre):
        for mascota in self.mascotas:
            if mascota.nombre.lower() == nombre.lower():
                return mascota
        return None  

    def listar_mascotas(self):
        print("Listado completo de pacientes ")
        if not self.mascotas:
            print("No hay mascotas registradas.")
            return

        for mascota in self.mascotas:
            print(f"Nombre: {mascota.nombre}, Especie: {mascota.especie}, Edad: {mascota.edad} años")
        

    def calcular_edad_promedio(self):
        if not self.mascotas:
            print("No hay mascotas registradas para calcular el promedio.")
            return None
        
        total_edades = sum(mascota.edad for mascota in self.mascotas)
        
        promedio = total_edades / len(self.mascotas)
        return promedio       