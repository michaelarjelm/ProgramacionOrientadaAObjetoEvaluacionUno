class Veterinaria:
    def __init__(self,nombre=""):
        self.nombre = nombre
        self.lista_mascotas = []

    def registra_mascota(self, mascota):
        self.lista_mascotas.append(mascota)
        print(f"{mascota.nombre} se ha registrado correctamente")




    def buscar_mascota(self, nombre):
        for mascota in self.lista_mascotas:
            if mascota.nombre == nombre:
                return mascota
        return None
    
    def listar_mascotas(self):
        for mascota in self.lista_mascotas:
            print(f"Nombre: {mascota.nombre}")



    def calcular_Edad(self):
        if len(self.lista_mascotas) == 0:
            print("No hay mascotas registradas")
            return 0  
        total = 0
        for m in self.lista_mascotas:
            total += m.edad
        promedio = total / len(self.lista_mascotas)
        print("Edad promedio:", round(promedio, 2))
        return promedio

                  





        