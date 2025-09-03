#Creamos las mascotas
class Mascota:
    def _init_(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

#Creamos la veterinaria
class Veterinaria:
    def _init_(self):
        self.mascotas = []

    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)
        print(f"\nMascota '{mascota.nombre}' registrada con éxito.")

    def buscar_mascota(self, nombre):
        for mascota in self.mascotas:
            if mascota.nombre.lower() == nombre.lower():
                return mascota
        return None  

    def listar_mascotas(self):
        print(f"\nListado completo de pacientes ")
        if not self.mascotas:
            print(f"\nNo hay mascotas registradas.")
            return

        for mascota in self.mascotas:
            print(f"\nNombre: '{mascota.nombre}', Especie: '{mascota.especie}', Edad: '{mascota.edad}' años.")
        

    def calcular_edad_promedio(self):
        if not self.mascotas:
            print("\nNo hay mascotas registradas para calcular el promedio.")
            return None
        
        total_edades = sum(mascota.edad for mascota in self.mascotas)
        
        promedio = total_edades (self.mascotas)
        return promedio 