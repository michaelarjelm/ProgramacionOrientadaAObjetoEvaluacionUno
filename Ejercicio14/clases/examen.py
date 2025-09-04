class Examen:
    def __init__(self, nombre):
        self.nombre = nombre
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def listar_preguntas(self):
        if self.preguntas:
            print(f"\n--- Lista de preguntas ---")
            print(f"Total preguntas: {len(self.preguntas)}\n")
            contador = 1
            for pregunta in self.preguntas:
                print(f"{contador}) {pregunta.pregunta}")
                contador +=1
        else:
            print("No hay preguntas para mostrar")

    def ver_respuesta(self, pregunta):
        if self.preguntas:
            if pregunta in self.preguntas:
                print(f"\nPregunta N°{self.preguntas.index(pregunta)+1}: '{pregunta.pregunta}")
                print(f"Respuesta: {pregunta.respuesta}")
            else:
                print("La pregunta no esta registrada")
        else:
            print("No hay preguntas resgistradas")
