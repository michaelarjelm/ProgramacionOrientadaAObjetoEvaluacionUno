from ejercicio1.libro import Libro, Biblioteca

biblio = Biblioteca()
libro1 = Libro(" Un secreto en mi colegio ", " Angelica Dossetti ", 4)
libro2 = Libro(" No toques a mi madre ", " Herve Mestron ", 3)

biblio.agregar(libro1)
biblio.agregar(libro2)

biblio.prestar("Un secreto en mi Colegio")
biblio.devolver("No toques a mi Madre ")

biblio.listar()
