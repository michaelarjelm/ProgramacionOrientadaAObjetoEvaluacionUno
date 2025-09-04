class Veterinaria:
    def __init__(self):
        self.mascotas = []

    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def buscar_por_nombre(self, nombre):
        for m in self.mascotas:
            if m.nombre == nombre:
                print(f"Encontrada: {m.nombre}, Especie: {m.especie}, Edad: {m.edad}")
                return
        print("Mascota no encontrada.")

    def listar_mascotas(self):
        for m in self.mascotas:
            print(f"Nombre: {m.nombre}, Especie: {m.especie}, Edad: {m.edad}")

    def calcular_edad_promedio(self):
        return sum(m.edad for m in self.mascotas) / len(self.mascotas) if self.mascotas else 0