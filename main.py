
#--------------Ejecicio 1----------------
#     las clases Libro y Biblioteca

# from ejercicio1.clases.libro import Libro
# from ejercicio1.clases.biblioteca import Biblioteca

# if __name__ == "__main__":
#     # Crear instancia de la biblioteca
#     mi_biblioteca = Biblioteca()

#     print("----------------------------------------------------------------------")
#     print("Bienvenidos a la Biblioteca de Pirque")
#     print("----------------------------------------------------------------------")
#     print()

#     # Mostrar catálogo inicial
#     mi_biblioteca.mostrar_catalogo()
#     print()

#     # Crear algunos libros
#     libro1 = Libro("La liebre y la tortuga", "Aesop", 3)
#     libro2 = Libro("Alicia en el País de las Maravillas", "Lewis Carroll", 2)
#     libro3 = Libro("La porota", "Antoine de Saint-Exupéry", 1)
#     print()

#     # Agregar libros a la biblioteca
#     mi_biblioteca.agregar_libros(libro1)
#     mi_biblioteca.agregar_libros(libro2)
#     mi_biblioteca.agregar_libros(libro3)
#     print()

#     # Mostrar catálogo después de agregar libros
#     mi_biblioteca.mostrar_catalogo()
#     print()
    
#     # Prestar algunos libros
#     mi_biblioteca.prestar_libro("La liebre y la tortuga")
#     mi_biblioteca.prestar_libro("la porota")
#     mi_biblioteca.prestar_libro("Alicia en el País de las Maravillas")
#     print()

#     # Mostrar catálogo después de prestar libros
#     mi_biblioteca.mostrar_catalogo()
#     print()

#     # Devolver un libro
#     mi_biblioteca.devolver_libro("La biblia")
#     print() 

#     # Mostrar catálogo final
#     mi_biblioteca.mostrar_catalogo()
#     print()

#--------------Ejecicio 2----------------

# from ejercicio2.clases.alumno import Alumno
# from ejercicio2.clases.curso import Curso

# if __name__ == "__main__":

#     print("----------------------------------------------------------------------")
#     print("Bienvenidos a los Cursos de programación")
#     print("----------------------------------------------------------------------")
#     print()

# # crear instancia de curso
#     curso_python = Curso("Python")
#     curso_java = Curso("Java")
#     curso_javascript = Curso("JavaScript")  

# # crear instancia de alumno
#     alumno1 = Alumno("Ruth Diaz")
#     alumno2 = Alumno("Alexander Murillo")
#     alumno3 = Alumno("Nancy Marchant")

# #ejecutar metodos del archvo curso.py
#     curso_python.inscribir_alumno(alumno1)
#     curso_python.inscribir_alumno(alumno2)
#     curso_python.inscribir_alumno(alumno3)
#     curso_java.inscribir_alumno(alumno1)
#     curso_javascript.inscribir_alumno(alumno2)
#     print()

#     curso_python.listar_alumnos()
#     print()
#     curso_java.listar_alumnos()
#     print()
#     curso_javascript.listar_alumnos()
#     print()

#     curso_python.remover_alumno(alumno2)
#     print()

#     curso_python.listar_alumnos() 
#     print()    

#--------------Ejecicio 3----------------

# from ejercicio3.clases.item import Item
# from ejercicio3.clases.pedido import Pedido

# if __name__ == "__main__":
#     print("----------------------------------------------------------------------")
#     print("Bienvenidos a Mi Tienda Online")
#     print("----------------------------------------------------------------------")
#     print()

#     pedido1 = Pedido()

#     item1 = Item("Camisa", 20.0, 2)
#     item2 = Item("Pantalones", 40.0, 1)
#     item3 = Item("Zapatos", 60.0, 1)

#     pedido1.agregar_item(item1)
#     pedido1.agregar_item(item2)
#     pedido1.agregar_item(item3)
#     print()

#     pedido1.calcular_total()
#     print()

#     pedido1.listar_items()
#     print()

#--------------Ejecicio 4----------------
# from ejercicio4.clases.sensor import Sensor

# if __name__ == "__main__":
#     print("----------------------------------------------------------------------")
#     print("Bienvenidos al Sistema de Monitoreo de Sensores")
#     print("----------------------------------------------------------------------")
#     print()

#     sensor_temperatura = Sensor("Sensor de Temperatura")

#     sensor_temperatura.registrar_valor(22.5)
#     sensor_temperatura.registrar_valor(23.0)
#     sensor_temperatura.registrar_valor(21.8)
#     sensor_temperatura.registrar_valor(24.1)
#     sensor_temperatura.registrar_valor(22.9)
#     print()

#     promedio = sensor_temperatura.obtener_promedio()
#     maximo = sensor_temperatura.obtener_maximo()
#     minimo = sensor_temperatura.obtener_minimo()

#     print(f"Promedio de mediciones: {promedio:.2f}")
#     print(f"Valor máximo: {maximo}")
#     print(f"Valor mínimo: {minimo}")
#     print()

#--------------Ejecicio 5----------------
# from ejercicio5.clases.pelicula import Pelicula
# from ejercicio5.clases.catalogo import Catalogo

# if __name__ == "__main__":
#     print("----------------------------------------------------------------------")
#     print("Bienvenidos al Catálogo de Blockbuster - Estrenos 2025")
#     print("----------------------------------------------------------------------")
#     print()

#     catalogo = Catalogo()

#     pelicula1 = Pelicula("Avatar 3", "Ciencia Ficción", 2025)
#     pelicula2 = Pelicula("Misión Imposible: Sentencia Final", "Acción", 2025)
#     pelicula3 = Pelicula("Inside Out 2", "Animación", 2025) 
#     pelicula4 = Pelicula("Jurassic World: Renacimiento", "Aventura", 2025)
#     pelicula5 = Pelicula("Downton Abbey 3", "Drama", 2025)

#     catalogo.agregar_pelicula(pelicula1)
#     catalogo.agregar_pelicula(pelicula2)
#     catalogo.agregar_pelicula(pelicula3)
#     catalogo.agregar_pelicula(pelicula4)
#     catalogo.agregar_pelicula(pelicula5)
#     print()

#     print("Listado de todas las películas:")
#     for pelicula in catalogo.listar_todas():
#         print(pelicula)
#     print()

#     genero_filtro = "Drama"
#     print(f"Películas del género '{genero_filtro}':")
#     for pelicula in catalogo.filtrar_por_genero(genero_filtro):
#         print(pelicula)
#     print()

#     titulo_buscar = "Avatar 3"
#     pelicula_encontrada = catalogo.buscar_por_titulo(titulo_buscar)
#     if pelicula_encontrada:
#         print(f"Película encontrada: {pelicula_encontrada}")
#     print()

#--------------Ejecicio 6----------------
# from ejercicio6.clases.auth import Auth
# from ejercicio6.clases.usuario import Usuario

# if __name__ == "__main__":
#     print("----------------------------------------------------------------------")
#     print("Bienvenidos al Sistema de Autenticación")
#     print("----------------------------------------------------------------------")
#     print()

#     auth_system = Auth()

#     auth_system.registrar("ruth", "password123")
#     auth_system.registrar("alexander", "securepass")
#     auth_system.registrar("nancy", "mypassword")
#     print()

#     auth_system.login("ruth", "password123")  
#     print()

#     print("Intento de login con credenciales incorrectas:")
#     auth_system.login("alexander", "wrongpass")  
#     print()

#     auth_system.login("nancy", "mypassword")  
#     print()

 
#--------------Ejecicio 7----------------
# from ejercicio7.clases.contacto import Contacto
# from ejercicio7.clases.agenda import Agenda     
# if __name__ == "__main__":
#     print("----------------------------------------------------------------------")
#     print("Bienvenidos a la Agenda de Contactos")
#     print("----------------------------------------------------------------------")
#     print()

#     agenda = Agenda()
#     contacto1 = Contacto("Ruth Diaz", "123456789", "rdiazmarchant@gmial.com")
#     contacto2 = Contacto("Alexander Murillo", "191919191", "Amurillod@gmial.com")

#     agenda.agregar_contacto(contacto1)
#     agenda.agregar_contacto(contacto2)  
#     print()

#     agenda.listar_contactos()
#     print()

#     nombre_buscar = "Ruth Diaz"
#     contacto_encontrado = agenda.buscar_contacto(nombre_buscar)
#     if contacto_encontrado:
#         print(f"Contacto encontrado: {contacto_encontrado}")    
#     print()

#     agenda.eliminar_contacto("Alexander Murillo")
#     print()

#     #probar contacto no registrado
#     agenda.eliminar_contacto("Nancy Marchant")
#     print()

#     agenda.listar_contactos()
#     print()
#--------------Ejecicio 8----------------

# from ejercicio8.clases.mesa import Mesa
# from ejercicio8.clases.restaurante import Restaurante
# if __name__ == "__main__":
#     print("----------------------------------------------------------------------")
#     print("Bienvenidos al Restaurante Aqui se come rico")
#     print("----------------------------------------------------------------------")
#     print()

#     restaurante = Restaurante("Aqui se come rico")

#     mesa1 = Mesa(1, 4)
#     mesa2 = Mesa(2, 2)
#     mesa3 = Mesa(3, 6)

#     restaurante.agregar_mesa(mesa1)
#     restaurante.agregar_mesa(mesa2)
#     restaurante.agregar_mesa(mesa3)
#     print()

#     restaurante.mostrar_estado_mesas()
#     print()

#     restaurante.reservar_mesa(2)
#     restaurante.reservar_mesa(3)
#     print()

#     restaurante.mostrar_estado_mesas()
#     print()

#     restaurante.liberar_mesa(2)
#     print()

#     restaurante.mostrar_estado_mesas()
#     print()

                        
# --------------Ejecicio 9----------------
# from ejercicio9.clases.producto import Producto
# from ejercicio9.clases.carrito import carrito
# if __name__ == "__main__":
#     print("----------------------------------------------------------------------")
#     print("Bienvenidos a la Tienda Online con Descuentos")
#     print("----------------------------------------------------------------------")
#     print()

#     carrito_compras = carrito()

#     producto1 = Producto("Cama", 800.00)
#     producto2 = Producto("Equipo de musica", 500.00)
#     producto3 = Producto("Auriculares", 150.00)

#     carrito_compras.agregar_producto(producto1, 1)
#     carrito_compras.agregar_producto(producto2, 2)
#     carrito_compras.agregar_producto(producto3, 3)
#     print()

#     carrito_compras.mostrar_carrito()
#     print()

#     total_sin_descuento = carrito_compras.calcular_total()
#     print(f"Total sin descuento: ${total_sin_descuento:.2f}")
#     print()

#     porcentaje_descuento = 10  
#     total_con_descuento = carrito_compras.aplicar_descuento(porcentaje_descuento)
#     print(f"Total con {porcentaje_descuento}% de descuento: ${total_con_descuento:.2f}")
#     print()


#--------------Ejecicio 10----------------

# from ejercicio10.clases.nota import Nota
# from ejercicio10.clases.estudiante import Estudiante        

# if __name__ == "__main__":
#     print("----------------------------------------------------------------------")
#     print("Bienvenidos, aqui se registran las notas de los estudiantes")
#     print("----------------------------------------------------------------------")
#     print()

#     estudiante1 = Estudiante("Ruth Diaz")

#     nota1 = Nota("Matemáticas", 70)
#     nota2 = Nota("Historia", 65)
#     nota3 = Nota("Ciencias", 60)

#     estudiante1.agregar_nota(nota1)
#     estudiante1.agregar_nota(nota2)
#     estudiante1.agregar_nota(nota3)
#     print()

#     print(f"Notas de {estudiante1.nombre}:")
#     estudiante1.mostrar_notas()
#     print()

#     promedio = estudiante1.calcular_promedio()
#     print(f"Promedio de calificaciones: {promedio:.2f}")
#     print()


#-------------ejercicios 11--------------------------

# from ejercicio11.clases.empresa import Empresa
# from ejercicio11.clases.empleado import Empleado    
# if __name__ == "__main__":

#     print("----------------------------------------------------------------------")
#     print("Bienvenidos a la Empresa del transnoche")
#     print("----------------------------------------------------------------------")
#     print()

#     empresa = Empresa()

#     empleado1 = Empleado("Ruth Diaz", 1000000)
#     empleado2 = Empleado("Alexander Murillo", 1200000)
#     empleado3 = Empleado("Nancy Marchant", 1300000)

#     empresa.contratar_empleado(empleado1)
#     empresa.contratar_empleado(empleado2)
#     empresa.contratar_empleado(empleado3)
#     print()

#     print("Listado de empleados:")
#     empresa.listar_empleados()
#     print()

#     gasto_total = empresa.gasto_total_sueldos()
#     print(f"Gasto total en sueldos de la empresa: ${gasto_total:.2f}")
#     print()
#-------------------ejecicio 12------------------------ 

# from ejercicio12.clases.cuenta import Cuenta
# from ejercicio12.clases.banco import Banco  
# if __name__ == "__main__":
#     print("----------------------------------------------------------------------")
#     print("Bienvenidos al Banco del Barrio")
#     print("----------------------------------------------------------------------")
#     print()

#     banco = Banco()

#     cuenta1 = Cuenta("Ruth Diaz", 100000)
#     cuenta2 = Cuenta("Alexander Murillo", 150000)
#     cuenta3 = Cuenta("Joaquin Díaz", 200000)

#     banco.abrir_cuenta(cuenta1)
#     banco.abrir_cuenta(cuenta2)
#     banco.abrir_cuenta(cuenta3)
#     print()

#     print("Estado inicial de las cuentas:")
#     banco.mostrar_estado_cuentas()
#     print()

#     banco.transferir_dinero("Ruth Diaz", "Alexander Murillo", 300)
#     print("Estado de las cuentas después de la transferencia:")
#     banco.mostrar_estado_cuentas()
#     print()

#     banco.transferir_dinero("Nancy Marchant", "Ruth Diaz", 500)
#     print("Estado de las cuentas después de la segunda transferencia:")
#     banco.mostrar_estado_cuentas()
#     print()

#-------------------ejercicios 13------------------------

# from ejercicio13.clases.mascota import Mascota
# from ejercicio13.clases.veterinaria import Veterinaria
# if __name__ == "__main__":
#     print("----------------------------------------------------------------------")
#     print("Bienvenidos a la Veterinaria Narices Frías, no tenemos fonasa")
#     print("----------------------------------------------------------------------")
#     print()

#     veterinaria = Veterinaria()

#     mascota1 = Mascota("Wudy", "Perro", 12)
#     mascota2 = Mascota("Pandy", "Gata", 9)
#     mascota3 = Mascota("Linda", "Perra", 9)

#     veterinaria.registrar_mascota(mascota1)
#     veterinaria.registrar_mascota(mascota2)
#     veterinaria.registrar_mascota(mascota3)
#     print()

#     print("Estas son todas las mascotas:")
#     veterinaria.listar_todas()
#     print()

#     print("Buscando una mascota por nombre:")
#     nombre_buscar = "Michi" #probando erroneo
#     mascota_encontrada = veterinaria.buscar_por_nombre(nombre_buscar)
#     if mascota_encontrada:
#         print(f"Mascota encontrada: Nombre: {mascota_encontrada.nombre}, Especie: {mascota_encontrada.especie}, Edad: {mascota_encontrada.edad} años")
#     else:
#         print(f"No se encontró ninguna mascota con el nombre '{nombre_buscar}'")
#     print()

#     edad_promedio = veterinaria.calcular_edad_promedio()
#     print(f"Edad promedio de las mascotas: {edad_promedio:.2f} años")
#     print()

#-------------------ejercicios 14------------------------
from ejercicio14.clases.pregunta import Pregunta
from ejercicio14.clases.examen import Examen    
if __name__ == "__main__":
    print("----------------------------------------------------------------------")
    print("Bienvenidos al sistema de Examen sorpresa")
    print("----------------------------------------------------------------------")
    print()

    examen = Examen()

    pregunta1 = Pregunta("¿Cuál es el primer libro de la Biblia?", "Genesis")
    pregunta2 = Pregunta("¿Cuanto es 1 + 2?", "3")
    pregunta3 = Pregunta("¿Que aparecio despues del diluvio?", "Un arcoiris")   

    examen.agregar_pregunta(pregunta1)
    examen.agregar_pregunta(pregunta2)
    examen.agregar_pregunta(pregunta3)
    print()

    print("Listado de preguntas del examen:")
    examen.listar_preguntas()
    print()

    total_preguntas = examen.contar_preguntas()
    print(f"Total de preguntas en el examen: {total_preguntas}")
    print()


print("fin del programaaaaaa por fin por fin no mas ejercicios  ")
