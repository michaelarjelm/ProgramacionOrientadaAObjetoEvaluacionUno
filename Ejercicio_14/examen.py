# Ejercicio 14 — Examen y Preguntas 
# Crea una clase Pregunta con enunciado y respuesta correcta. Crea una clase Examen con una lista 
# de preguntas. Agrega métodos para añadir preguntas, listar preguntas y contar el total de 
# preguntas del examen. 

from pregunta import Pregunta

class Examen:
    def __init__(self):
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)
        print(f" Pregunta agregada: {pregunta.enunciado}")

    def listar_preguntas(self):
        if not self.preguntas:
            print(" No hay preguntas en el examen.")
        else:
            print("\n--- Preguntas del Examen ---")
            for idx, p in enumerate(self.preguntas, 1):
                print(f"{idx}. {p.enunciado} (Respuesta correcta: {p.respuesta_correcta})")

    def total_preguntas(self):
        return len(self.preguntas)
