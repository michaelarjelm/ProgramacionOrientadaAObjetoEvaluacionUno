from statistics import mean
from math import trunc

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
                print(f"* Nombre: {paciente.nombre} | Especie: {paciente.especie} | Edad: {paciente.edad}")
            else:
                print("\nError de busqueda")
                print(f"El paciente '{paciente.nombre}' no esta registrado")
        else:
            print("\nError de busqueda")
            print("No hay pacientes inscritos")

    def ver_pacientes(self):
        if self.pacientes:
            print("\n--- Lista de pacientes ---\n")
            for paciente in self.pacientes:
                print(f"* Nombre: {paciente.nombre:13} | Especie: {paciente.especie:8} | Edad: {paciente.edad}")
        else:
            print("\nError de vizualizacion")
            print("No hay pacientes inscritos")

    def promedio_edades(self):
        if self.pacientes:
            promedio = []
            for paciente in self.pacientes:
                promedio.append(paciente.edad)
            print(f"\nPromedio de edades: {trunc(mean(promedio))} años")
        else:
            print("\nError de vizualizacion de promedios")
            print("No hay pacientes inscritos para promediar")
