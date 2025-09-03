class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} - ({self.especie}) - {self.edad} años" 

class Veterinaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pacientes = [] # ~ Lista para almacenar las mascotas

    def registrarMascota(self, mascota: Mascota):
        self.pacientes.append(mascota)
        print(f"¡{mascota.nombre} fue registrada con éxito!")

    def buscarMascota(self, nombre):
        for mascota in self.pacientes: # ~ Itera sobre la lista de mascotas
            if mascota.nombre.lower() == nombre.lower(): # ~ Comparación sin distinción de mayúsculas/minúsculas
                print(f"{mascota} encontrada en el registro.")
                return
        print("Mascota no encontrada en el registro.")

    def listarMascotas(self):
        if not self.pacientes:
            print("No hay mascotas registradas.")
        else:
            for mascota in self.pacientes:
                print(f"{mascota}")

    def edadPromedio(self):
        if not self.pacientes: # ~ Verifica si la lista está vacía
            print("No hay mascotas registradas.")
            return 0.0
        
        totalEdades = sum(mascota.edad for mascota in self.pacientes) # ~ Suma las edades de todas las mascotas
        promedio = totalEdades / len(self.pacientes)
        
        print(f"La edad promedio es:{promedio:.1f} años")
        return promedio