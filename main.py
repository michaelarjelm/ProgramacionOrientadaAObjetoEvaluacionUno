# # Desarrolo Evaluacion 1

# # Ejercicio_1

# from libro import Libro
# from biblioteca import Biblioteca

# if __name__ == "__main__":
#     biblioteca = Biblioteca()

#     # Crear libros
#     libro1 = Libro("Los Miserables", "Victor hugo", 3)
#     libro2 = Libro("La Odisea", "Homero", 2)

#     # Agregar libros
#     biblioteca.agregar_libro(libro1)
#     biblioteca.agregar_libro(libro2)

#     # Mostrar libros
#     biblioteca.mostrar_libros()

#     # Prestar un libro
#     biblioteca.prestar_libro("Los Miserables")
#     biblioteca.mostrar_libros()

#     # Devolver un libro
#     biblioteca.devolver_libro("Los Miserables")
#     biblioteca.mostrar_libros()

# # Ejercicio_2

# from alumno import Alumno
# from curso import Curso

# if __name__ == "__main__":
#     curso_python = Curso("Python Básico")

#     # Crear alumnos
#     alumno1 = Alumno("Soledad Miranda")
#     alumno2 = Alumno("Juan Pérez")
#     alumno3 = Alumno("María López")

#     # Inscribir alumnos
#     curso_python.inscribir_alumno(alumno1)
#     curso_python.inscribir_alumno(alumno2)
#     curso_python.inscribir_alumno(alumno3)

#     # Listar alumnos
#     curso_python.listar_alumnos()

#     # Remover un alumno
#     curso_python.remover_alumno("Juan Pérez")
#     curso_python.listar_alumnos()

# # Ejercico_3

# from item import Item
# from pedido import Pedido

# if __name__ == "__main__":
#     pedido = Pedido()

#     # Crear ítems
#     item1 = Item("Camisa", 15000, 2)
#     item2 = Item("Pantalón", 25000, 1)
#     item3 = Item("Zapatos", 50000, 1)

#     # Agregar ítems al pedido
#     pedido.agregar_item(item1)
#     pedido.agregar_item(item2)
#     pedido.agregar_item(item3)

#     # Mostrar pedido y total
#     pedido.mostrar_pedido()

# # Ejercicio_4

# from sensor import Sensor

# if __name__ == "__main__":
#     sensor_temp = Sensor("Temperatura")

#     # Registrar valores
#     sensor_temp.registrar_valor(23.5)
#     sensor_temp.registrar_valor(25.1)
#     sensor_temp.registrar_valor(22.8)
#     sensor_temp.registrar_valor(24.0)

#     # Mostrar resultados
#     sensor_temp.mostrar_mediciones()

# # Ejercico_5

# from pelicula import Pelicula
# from catalogo import Catalogo

# if __name__ == "__main__":
#     catalogo = Catalogo()

#     # Crear películas
#     peli1 = Pelicula("Inception", "Ciencia Ficción", 2010)
#     peli2 = Pelicula("Titanic", "Romance", 1997)
#     peli3 = Pelicula("The Matrix", "Ciencia Ficción", 1999)
#     peli4 = Pelicula("La La Land", "Musical", 2016)

#     # Agregar películas al catálogo
#     catalogo.agregar_pelicula(peli1)
#     catalogo.agregar_pelicula(peli2)
#     catalogo.agregar_pelicula(peli3)
#     catalogo.agregar_pelicula(peli4)

#     # Listar todas
#     catalogo.listar_todas()

#     # Filtrar por género
#     catalogo.filtrar_por_genero("Ciencia Ficción")

#     # Buscar por título
#     catalogo.buscar_por_titulo("Titanic")
#     catalogo.buscar_por_titulo("Avatar")

# # Ejercicio_6

# from auth import Auth

# if __name__ == "__main__":
#     auth_system = Auth()

#     # Registrar usuarios
#     auth_system.registrar_usuario("soledad", "1234")
#     auth_system.registrar_usuario("juan", "abcd")
#     auth_system.registrar_usuario("soledad", "5678")  # Intento duplicado

#     # Listar de usuarios
#     auth_system.listar_usuarios()

#     # Intentos de login
#     auth_system.login("soledad", "1234")  # Correcto
#     auth_system.login("juan", "1234")     # Incorrecto
#     auth_system.login("maria", "abcd")    # Usuario no registrado

# # Ejercicio_7

# from agenda import Agenda
# from contacto import Contacto

# if __name__ == "__main__":
#     agenda = Agenda()

#     # Crear contactos
#     c1 = Contacto("Soledad Miranda", "987654321", "soledad@mail.com")
#     c2 = Contacto("Juan Pérez", "912345678", "juan@mail.com")
#     c3 = Contacto("María López", "923456789", "maria@mail.com")

#     # Agregar contactos
#     agenda.agregar_contacto(c1)
#     agenda.agregar_contacto(c2)
#     agenda.agregar_contacto(c3)
#     agenda.agregar_contacto(c1)  # Intento duplicado

#     # Listar contactos
#     agenda.listar_contactos()

#     # Buscar un contacto
#     agenda.buscar_contacto("Juan Pérez")

#     # Eliminar un contacto
#     agenda.eliminar_contacto("María López")
#     agenda.listar_contactos()
    
#     # Ejercicio_8
    
#     from restaurante import Restaurante
# from mesa import Mesa

# if __name__ == "__main__":
#     restaurante = Restaurante()

#     # Crear mesas
#     m1 = Mesa(1, 4)
#     m2 = Mesa(2, 2)
#     m3 = Mesa(3, 6)

#     # Agregar mesas al restaurante
#     restaurante.agregar_mesa(m1)
#     restaurante.agregar_mesa(m2)
#     restaurante.agregar_mesa(m3)

#     # Mostrar estado inicial
#     restaurante.mostrar_estado_mesas()

#     # Reservar mesas
#     restaurante.reservar_mesa(2)
#     restaurante.reservar_mesa(3)

#     # Mostrar estado después de reservas
#     restaurante.mostrar_estado_mesas()

#     # Liberar una mesa
#     restaurante.liberar_mesa(2)
#     restaurante.mostrar_estado_mesas()

#  # Ejercicio_9
    
# from producto import Producto
# from carrito import Carrito

# if __name__ == "__main__":
#     carrito = Carrito()

#     # Crear productos
#     p1 = Producto("Camisa", 15000)
#     p2 = Producto("Pantalón", 25000)
#     p3 = Producto("Zapatos", 50000)

#     # Agregar productos al carrito
#     carrito.agregar_producto(p1, 2)
#     carrito.agregar_producto(p2, 1)
#     carrito.agregar_producto(p3, 1)

#     # Mostrar carrito y total
#     carrito.mostrar_carrito()

#     # Aplicar descuento
#     descuento = 10  # 10%
#     total_con_descuento = carrito.aplicar_descuento(descuento)
#     print(f" Total con {descuento}% de descuento: ${total_con_descuento}")

# #  Ejercicio_10
    
#     from estudiante import Estudiante
# from nota import Nota

# if __name__ == "__main__":
#     estudiante1 = Estudiante("Soledad Miranda")

#     # Agregar notas
#     estudiante1.agregar_nota(Nota("Matemáticas", 6.5))
#     estudiante1.agregar_nota(Nota("Historia", 5.8))
#     estudiante1.agregar_nota(Nota("Ciencias", 7.0))

#     # Mostrar notas y promedio
#     estudiante1.mostrar_notas()

# Ejercicio_11

# from empresa import Empresa
# from empleado import Empleado

# if __name__ == "__main__":
#     empresa = Empresa()

#     # Contratar empleados
#     e1 = Empleado("Soledad Miranda", 1200000)
#     e2 = Empleado("Juan Pérez", 1500000)
#     e3 = Empleado("María López", 1300000)

#     empresa.contratar_empleado(e1)
#     empresa.contratar_empleado(e2)
#     empresa.contratar_empleado(e3)

#     # Listar empleados
#     empresa.listar_empleados()

#     # Calcular gasto total en sueldos
#     print(f"\n Gasto total en sueldos: ${empresa.gasto_total_sueldos()}")

# # Ejercicio_12

# from banco import Banco
# from cuenta import Cuenta

# if __name__ == "__main__":
#     banco = Banco()

#     # Abrir cuentas
#     c1 = Cuenta("Soledad Miranda", 50000)
#     c2 = Cuenta("Juan Pérez", 30000)
#     c3 = Cuenta("María López", 20000)

#     banco.abrir_cuenta(c1)
#     banco.abrir_cuenta(c2)
#     banco.abrir_cuenta(c3)

#     # Mostrar estado inicial
#     banco.mostrar_estado_cuentas()

#     # Transferencias
#     banco.transferir("Soledad Miranda", "Juan Pérez", 15000)
#     banco.transferir("María López", "Soledad Miranda", 5000)

#     # Mostrar estado final
#     banco.mostrar_estado_cuentas()

# # Ejercicio_13

# from veterinaria import Veterinaria
# from mascota import Mascota

# if __name__ == "__main__":
#     vet = Veterinaria()

#     # Registrar mascotas
#     m1 = Mascota("Fido", "Perro", 5)
#     m2 = Mascota("Mia", "Gato", 3)
#     m3 = Mascota("Luna", "Conejo", 2)

#     vet.registrar_mascota(m1)
#     vet.registrar_mascota(m2)
#     vet.registrar_mascota(m3)

#     # Listar todas las mascotas
#     vet.listar_mascotas()

#     # Buscar mascota
#     vet.buscar_mascota("Mia")
#     vet.buscar_mascota("Rex")  # No existe

#     # Edad promedio
#     print(f"\n Edad promedio de las mascotas: {vet.edad_promedio():.2f} años")

# # Ejercicio_14

# from examen import Examen
# from pregunta import Pregunta

# if __name__ == "__main__":
#     examen = Examen()

#     # Agregar preguntas
#     p1 = Pregunta("¿Cuál es la capital de Chile?", "Santiago")
#     p2 = Pregunta("¿2 + 2 =", "4")
#     p3 = Pregunta("¿Color del cielo?", "Azul")

#     examen.agregar_pregunta(p1)
#     examen.agregar_pregunta(p2)
#     examen.agregar_pregunta(p3)

#     # Listar preguntas
#     examen.listar_preguntas()

#     # Total de preguntas
#     print(f"\n Total de preguntas del examen: {examen.total_preguntas()}")
