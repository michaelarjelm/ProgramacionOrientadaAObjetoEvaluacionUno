#Clase Veterinaria
class Veterinaria:
    def __init__(self):
        self.mascotas = []

    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)
        print(f"Mascota '{mascota.nombre}' registrada con éxito.")

    def buscar_por_nombre(self, nombre):
        resultados = [m for m in self.mascotas if m.nombre.lower() == nombre.lower()]
        if resultados:
            print("Resultado(s) encontrado(s):")
            for mascota in resultados:
                print(mascota)
        else:
            print(f"No se encontró ninguna mascota con el nombre '{nombre}'.")

    def listar_mascotas(self):
        if not self.mascotas:
            print("No hay mascotas registradas.")
        else:
            print("Lista de mascotas registradas:")
            for mascota in self.mascotas:
                print(mascota)

    def edad_promedio(self):
        if not self.mascotas:
            print("No hay mascotas para calcular la edad promedio.")
            return 0
        total_edad = sum(m.edad for m in self.mascotas)
        promedio = total_edad / len(self.mascotas)
        print(f"Edad promedio de las mascotas: {promedio:.2f} años")
        return promedio
