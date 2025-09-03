class Mascota:
    """Clase que representa una mascota con nombre, especie y edad."""
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    def __str__(self):
        """Devuelve una representación en cadena del objeto Mascota."""
        return f"Nombre: {self.nombre} | Especie: {self.especie} | Edad: {self.edad} años"
class Veterinaria:
    """Clase que gestiona un registro de mascotas."""
    def __init__(self):
        self.mascotas = []
    def registrar_mascota(self, mascota):
        """Agrega una mascota al registro de la veterinaria."""
        self.mascotas.append(mascota)
        print(f"✅ Mascota '{mascota.nombre}' registrada con éxito.")
    def buscar_mascota(self, nombre):
        """Busca una mascota por su nombre y devuelve el objeto si lo encuentra."""
        for mascota in self.mascotas:
            if mascota.nombre.lower() == nombre.lower():
                print(f"✅ Mascota encontrada: {mascota}")
                return mascota
        print(f"❌ Mascota con el nombre '{nombre}' no encontrada.")
        return None
    def listar_mascotas(self):
        """Muestra el listado completo de mascotas registradas."""
        print("\n📋 Listado de Mascotas:")
        if not self.mascotas:
            print("No hay mascotas registradas.")
        else:
            for mascota in self.mascotas:
                print(f"- {mascota}")
    def calcular_edad_promedio(self):
        """Calcula y devuelve la edad promedio de las mascotas."""
        if not self.mascotas:
            return 0
        total_edades = sum(mascota.edad for mascota in self.mascotas)
        return total_edades / len(self.mascotas)