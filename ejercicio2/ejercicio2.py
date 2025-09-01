class Alumno:
    def __init__(self,inscribir,remover):
        curso = ["carlos","juan","alberto","pedro"]
        self.inscribir = inscribir
        self.remover = remover
        curso.append(self.inscribir)
        curso.remove(self.remover)
        for alumno in curso:
            print(alumno)
