class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}"


class Veterinaria:
    def __init__(self):
        self.mascotas = []

    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)
        print(f"Mascota {mascota.nombre} registrada.")

    def buscar_mascota(self, nombre):
        for mascota in self.mascotas:
            if mascota.nombre == nombre:
                return mascota
        print("Mascota no encontrada.")
        return None

    def listar_mascotas(self):
        if not self.mascotas:
            print("No hay mascotas registradas.")
            return
        print("Listado de mascotas:")
        for mascota in self.mascotas:
            print(mascota)

    def calcular_edad_promedio(self):
        if not self.mascotas:
            print("No hay mascotas registradas para calcular la edad promedio.")
            return 0
        edades = [mascota.edad for mascota in self.mascotas]
        edad_promedio = sum(edades) / len(edades)
        print(f"La edad promedio de las mascotas es: {edad_promedio:.2f} años")
        return edad_promedio


#Ejemplo de uso
veterinaria = Veterinaria()

#Registrar mascotas
mascota1 = Mascota("Firulais", "Perro", 3)
mascota2 = Mascota("Misifus", "Gato", 5)
mascota3 = Mascota("Rocky", "Perro", 7)

veterinaria.registrar_mascota(mascota1)
veterinaria.registrar_mascota(mascota2)
veterinaria.registrar_mascota(mascota3)

#Buscar mascota
mascota_encontrada = veterinaria.buscar_mascota("Misifus")
if mascota_encontrada:
    print(f"Mascota encontrada: {mascota_encontrada}")

#Listar mascotas
veterinaria.listar_mascotas()

#Calcular edad promedio
veterinaria.calcular_edad_promedio()

#ejercicio 14

