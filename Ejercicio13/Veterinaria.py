class Veterinaria:
    def __init__(self):
        self.mascotas = []

    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def buscar_por_nombre(self, nombre):
        for mascota in self.mascotas:
            if mascota.nombre.lower() == nombre.lower():
                return mascota
        return None

    def listar_todas(self):
        if not self.mascotas:
            return "No hay mascotas registradas."
        return "\n".join(str(mascota) for mascota in self.mascotas)

    def calcular_edad_promedio(self):
        if not self.mascotas:
            return 0
        total_edad = sum(mascota.edad for mascota in self.mascotas)
        return total_edad / len(self.mascotas)