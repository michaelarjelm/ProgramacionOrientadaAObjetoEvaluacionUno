# Ejercicio 13 — Veterinaria y Mascotas
# Crea una clase Mascota con nombre, especie y edad. Crea una clase Veterinaria que permita
# registrar mascotas, buscar por nombre, listar todas y calcular la edad promedio de las mascotas.

class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

class Veterinaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pacientes = []

    def registrar(self, paciente):
        self.pacientes.append(paciente)
        print(f"\nPaciente '{paciente.nombre}' registrado con exito.")

    def buscar(self, paciente):
        if self.pacientes:
            if paciente in self.pacientes:
                print("\n--- Resultado busqueda ---")

    def ver_pacientes(self):
        pass

    def promedio_edades(self):
        pass