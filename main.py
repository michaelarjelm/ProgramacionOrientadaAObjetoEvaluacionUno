from ejercicio1.libro import Libro, Biblioteca

biblio = Biblioteca()
libro1 = Libro("1984", "George Orwell", 3)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 2)

biblio.agregar(libro1)
biblio.agregar(libro2)

biblio.prestar("1984")
biblio.devolver("El Principito")

biblio.listar()
