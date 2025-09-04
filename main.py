# Crear biblioteca y libros
biblio = Biblioteca()

libro1 = Libro("Harry Potter", "J.K. Rowling", 2)
libro2 = Libro("El Hobbit", "J.R.R. Tolkien", 1)

# Agregar libros
biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)

# Mostrar libros
biblio.mostrar_libros()

# Prestar y devolver libros
biblio.prestar_libro("Harry Potter")
biblio.devolver_libro("Harry Potter")
biblio.mostrar_libros()