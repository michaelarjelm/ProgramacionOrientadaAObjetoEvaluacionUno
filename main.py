## ==== desarrollo de ejercicio_1 ==== ##
print ("_______Ejercicio UNO_______")

from  ejercicio_1.libro_biblioteca import Libro, Biblioteca

mi_biblioteca = Biblioteca()

libro1 = Libro("Cien años de soledad.", "Gabriel Garcia Marquez.", 5)
libro2 = Libro("El corazon delator.", "Edgar Allan Poe.", 7)
libro3 = Libro("La metamorfosis.", "Franz kafka.",3)

mi_biblioteca.agregar(libro1)
mi_biblioteca.agregar(libro2)
mi_biblioteca.agregar(libro3)

mi_biblioteca.prestar("El corazon delator.")

mi_biblioteca.devolver("Cien años de soledad.")

mi_biblioteca.mostrar()

## ==== desarrollo de ejercicio_2 ==== ##
print ("_______Ejercicio DOS_______")

from ejercicio_2.alumno_curso import alumno, curso

alumno1 = alumno("Samuel Morales")
alumno2 = alumno("Camilo Candia")
alumno3 = alumno("Joaquin Navarrete")

curso_basico = curso("Serigrafia")
  
curso_basico.inscribir(alumno1)
curso_basico.inscribir(alumno2)
curso_basico.inscribir(alumno3)

curso_basico.remover(alumno2)

curso_basico.listar_alumno()
