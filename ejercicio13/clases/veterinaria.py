from ejercicio13.clases.mascota import Mascota


class Veterinaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mascotas =[]
        
    def registrar_mascota(self, nombre, especie, edad):
        self.mascotas.append(Mascota(nombre, especie, edad))
        print(f"Mascota registrada: {nombre}({especie},{edad} años.)")
        
    
    def buscar_mascota(self,nombre):
        for mascota in self.mascotas:
            if mascota.nombre.lower() == nombre.lower():
                print("Mascota encontrada:", mascota)
                return mascota
        print(f"No se encuentró a la mascota llamada '{nombre}'.")
        return None
    
    def listar_mascotas(self):
        if not self.mascotas:
            print("No hay mascotas ingresadas en nuestro sistema")
        else:
            print(f"Mascotas en la veterinaria {self.nombre}:")
            for mascota in self.mascotas:
                print("- "+ str(mascota))
                
    def calcular_edad_promedio(self):
        if not self.mascotas:
            print("No hay mascotas para calcular el promedio.")
            return None
        promedio = sum(m.edad for m in self.mascotas) / len(self.mascotas)
        print(f"Edad promedio: {promedio:.1f} años")
        return promedio
    
            
        
        
    