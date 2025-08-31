# Ejercicio 2 — Alumno y Curso
# Crea una clase Alumno con nombre. Crea una clase Curso con nombre y una lista de alumnos, que
# permita inscribir, remover y listar alumnos

class Curso:
        def __init__(self,nombre_curso):
                self.nombre_curso = nombre_curso
                self.lista_alumnos = []


        def inscribir_alumno(self,alumno):
                self.lista_alumnos.append(alumno)



        def listado_alumnos(self):
                for alumno in self.lista_alumnos:
                        print(alumno)

        
        def quitar_alumno(self):
                nombre_completo = input("ingresa el nombre completo del alumno a quitar de la lista : ").strip()
                
                
                for alumno in self.lista_alumnos:
                        if nombre_completo.lower() == f"{alumno.nombres} {alumno.apellidos}".lower():
                                self.lista_alumnos.remove (alumno)
                                print("Se han quitado de la lista el alumno solicitado.")    
                                break
                        
                else:
                        print("El alumno ingresado no se encuentra registrado en la lista.")