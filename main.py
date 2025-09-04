# # Desarrollo evaluacion 1 

# # Ejercicio_1: Biblioteca-libro

# libro1 = Libro("Nubes de talco", "Amanda Baeza", 5)
# libro2 = Libro("Peklo", "Sukinapan", 7)
# libro3 = Libro("Tekkonkinkreet", "Taiyo Matsumoto", 3)

# bibliobus = Biblioteca("Bibliobus")

# bibliobus.agregar_libro(libro1)
# bibliobus.agregar_libro(libro2)
# print("--------------------------------")
# bibliobus.prestamo(libro1, 3)
# print("--------------------------------")
# bibliobus.devolucion(libro1, 2)
# print("--------------------------------")
# bibliobus.listar_libros()

# # Ejercicio_2: alumno-curso

# if __name__ == "__main__":
#     curso_python = Curso("Python Básico")

#     alumno1 = Alumno("Juan")
#     alumno2 = Alumno("Ana")
#     alumno3 = Alumno("Luis")

#     curso_python.inscribir(alumno1)
#     curso_python.inscribir(alumno2)
#     curso_python.inscribir(alumno3)

#     curso_python.listar_alumnos()

#     curso_python.remover(alumno2)
#     curso_python.listar_alumnos()

#     # Ejercicio_3: Pedido e item

# if __name__ == "__main__":
#     pedido = Pedido()

#     item1 = Item("Camisa", 15.99, 2)
#     item2 = Item("Pantalón", 25.50, 1)
#     item3 = Item("Calcetines", 5.00, 5)

#     pedido.agregar_item(item1)
#     pedido.agregar_item(item2)
#     pedido.agregar_item(item3)

#     pedido.mostrar_pedido()

#     # #Ejercicio_4: Sensor y Mediciones

# from ejercicio4.Sensor_Mediciones import Sensor

# # --- Creación del Sensor ---
# # Sensor para medir la temperatura en san bernardo.
# sensor_san_bernardo = Sensor(nombre="Temperatura Ambiental - Puente Alto")
# print(f"Sensor '{sensor_san_bernardo.nombre}' creado exitosamente.")

# # --- Registro de Mediciones ---

# print("\nRegistrando mediciones del día...")
# sensor_san_bernardo.registrar_medicion(12.5)
# sensor_san_bernardo.registrar_medicion(12.5)
# sensor_san_bernardo.registrar_medicion(18.2)
# sensor_san_bernardo.registrar_medicion(21.8)
# sensor_san_bernardo.registrar_medicion(17.6) 
# sensor_san_bernardo.registrar_medicion(14.1) 

# # Mostramos todas las mediciones registradas.
# print(f"Mediciones registradas: {sensor_san_bernardo.mediciones}")

# # --- Cálculos ---
# # Usamos los métodos de la clase para obtener y mostrar las estadísticas.
# print("\nCalculando reporte meteorológico...")
# promedio_dia = sensor_san_bernardo.obtener_promedio()
# maxima_dia = sensor_san_bernardo.obtener_maximo()
# minima_dia = sensor_san_bernardo.obtener_minimo()

# # --- Impresión del Reporte ---
# print(f"\n--- 🌡️ Reporte del Día: {sensor_san_bernardo.nombre} ---")
# print(f"  - Temperatura Promedio: {promedio_dia:.1f}°C") # Usamos :.1f para 1 decimal
# print(f"  - Temperatura Máxima: {maxima_dia}°C")
# print(f"  - Temperatura Mínima: {minima_dia}°C")
# print("-------------------------------------------------")



# #  ejercicio_5: Catálogo y Película.

# from catalogo import Catalogo

# def main():
#     catalogo = Catalogo()

#     catalogo.agregar_pelicula("Inception", "Ciencia ficción", 2010)
#     catalogo.agregar_pelicula("Titanic", "Romance", 1997)
#     catalogo.agregar_pelicula("The Matrix", "Ciencia ficción", 1999)
#     catalogo.agregar_pelicula("El Padrino", "Drama", 1972)

#     catalogo.listar_peliculas()

#     genero = "Ciencia ficción"
#     print(f"\nPelículas del género '{genero}':")
#     for pelicula in catalogo.filtrar_por_genero(genero):
#         print(pelicula)

#     titulo = "Titanic"
#     print(f"\nBuscando película por título '{titulo}':")
#     pelicula = catalogo.buscar_por_titulo(titulo)
#     if pelicula:
#         print(pelicula)
#     else:
#         print("Película no encontrada.")

# if __name__ == "__main__":
#     main()



#     #Ejercicio_6: Autenticacion-Usuario

# from autentificacion import Auth

# def main():
#     auth = Auth()

#     # Registrar usuarios
#     auth.registrar_usuario("juan123", "pass123")
#     auth.registrar_usuario("maria456", "password456")

#     # Intentos de login
#     auth.login("juan123", "pass123")        # Éxito
#     auth.login("juan123", "wrongpass")      # Error contraseña
#     auth.login("usuario_inexistente", "abc")  # Usuario no encontrado

# if __name__ == "__main__":
#     main()

    
#     #Ejercicio_7: Agenda-Contacto

# from agenda import Agenda

# def main():
#     agenda = Agenda()

#     agenda.agregar_contacto("Ana", "555-1234", "ana@example.com")
#     agenda.agregar_contacto("Luis", "555-5678", "luis@example.com")
#     agenda.agregar_contacto("Ana", "555-4321", "ana2@example.com")  # Dos contactos con mismo nombre

#     agenda.listar_contactos()

#     nombre_buscar = "Ana"
#     print(f"\nBuscando contactos con nombre '{nombre_buscar}':")
#     encontrados = agenda.buscar_contacto(nombre_buscar)
#     for c in encontrados:
#         print(c)

#     print(f"\nEliminando contactos con nombre '{nombre_buscar}':")
#     agenda.eliminar_contacto(nombre_buscar)

#     agenda.listar_contactos()

# if __name__ == "__main__":
#     main()


#     #Ejercicio_8: Mesa-Restaurante

# from restaurante import Restaurante

# def main():
#     restaurante = Restaurante()

#     restaurante.agregar_mesa(1, 4)
#     restaurante.agregar_mesa(2, 2)
#     restaurante.agregar_mesa(3, 6)

#     restaurante.mostrar_estado_mesas()

#     print("\nReservando mesa 2:")
#     restaurante.reservar_mesa(2)

#     print("\nEstado actualizado:")
#     restaurante.mostrar_estado_mesas()

#     print("\nLiberando mesa 2:")
#     restaurante.liberar_mesa(2)

#     print("\nEstado actualizado:")
#     restaurante.mostrar_estado_mesas()

# if __name__ == "__main__":
#     main()
   
    
#     # Ejercicio_9: Carrito-Producto

#     from producto import Producto
# from carrito import Carrito

# def main():
#     carrito = Carrito()

#     p1 = Producto("Manzana", 0.5)
#     p2 = Producto("Leche", 1.2)
#     p3 = Producto("Pan", 0.8)

#     carrito.agregar_producto(p1, 4)
#     carrito.agregar_producto(p2, 2)
#     carrito.agregar_producto(p3, 1)

#     carrito.mostrar_carrito()

#     descuento = 10  # 10%
#     total_desc = carrito.aplicar_descuento(descuento)
#     print(f"\nTotal con {descuento}% de descuento: ${total_desc:.2f}")

# if __name__ == "__main__":
#     main()
    
    
#     #Ejercicio_10: Estudiante-Nota

# from estudiante import Estudiante

# def main():
#     estudiante = Estudiante("Carlos")

#     estudiante.agregar_nota("Matemáticas", 85)
#     estudiante.agregar_nota("Historia", 90)
#     estudiante.agregar_nota("Ciencias", 78)

#     estudiante.mostrar_notas()

#     promedio = estudiante.calcular_promedio()
#     print(f"\nPromedio de calificaciones: {promedio:.2f}")

# if __name__ == "__main__":
#     main()
    
    
#     #Ejercicio_11: Empleado-Empresa

# from empresa import Empresa

# def main():
#     empresa = Empresa()

#     empresa.contratar_empleado("Ana", 1500)
#     empresa.contratar_empleado("Luis", 1800)
#     empresa.contratar_empleado("María", 1700)

#     empresa.listar_empleados()

#     gasto_total = empresa.calcular_gasto_sueldos()
#     print(f"\nGasto total en sueldos: ${gasto_total:.2f}")

# if __name__ == "__main__":
#     main()
    
    
#     #Ejercicio_12: Banco-Cuenta

# from banco import Banco

# def main():
#     banco = Banco()

#     banco.abrir_cuenta("Juan", 1000)
#     banco.abrir_cuenta("María", 500)
#     banco.abrir_cuenta("Luis", 300)

#     banco.mostrar_estado_cuentas()

#     print("\nTransferencia de Juan a María por $200:")
#     banco.transferir("Juan", "María", 200)

#     banco.mostrar_estado_cuentas()

#     print("\nIntento de transferencia con fondos insuficientes:")
#     banco.transferir("Luis", "Juan", 400)

# if __name__ == "__main__":
#     main()

#      #Ejercicio_13: Mascota-Veterinaria

# from veterinaria import Veterinaria

# def main():
#     vet = Veterinaria()

#     vet.registrar_mascota("Firulais", "Perro", 5)
#     vet.registrar_mascota("Michi", "Gato", 3)
#     vet.registrar_mascota("Nemo", "Pez", 1)

#     vet.listar_mascotas()

#     nombre_buscar = "Michi"
#     print(f"\nBuscando mascota por nombre '{nombre_buscar}':")
#     mascota = vet.buscar_por_nombre(nombre_buscar)
#     if mascota:
#         print(mascota)
#     else:
#         print("Mascota no encontrada.")

#     promedio = vet.calcular_edad_promedio()
#     print(f"\nEdad promedio de las mascotas: {promedio:.2f} años")

# if __name__ == "__main__":
#     main()

#     #Ejercicio_14: Examen-Pregunta

# from examen import Examen

# def main():
#     examen = Examen()

#     examen.agregar_pregunta("¿Cuál es la capital de Francia?", "París")
#     examen.agregar_pregunta("¿Cuánto es 2 + 2?", "4")
#     examen.agregar_pregunta("¿Qué lenguaje se usa para programación orientada a objetos?", "Python")

#     examen.listar_preguntas()

#     print(f"\nTotal de preguntas en el examen: {examen.total_preguntas()}")

# if __name__ == "__main__":
#     main()
