"""Ejercicio 1: Sistema de Gestión de Biblioteca"""
# Importar las clases Libro y Biblioteca desde el módulo Clases_De_Libro
from Ejercicio1.Clases_De_Libro import Libro, Biblioteca
# Crear una instancia de la biblioteca
mi_biblioteca = Biblioteca()
# Crear instancias de libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 3)
libro2 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", 5)
# Agregar libros a la biblioteca
mi_biblioteca.agregar_libro(libro1)
mi_biblioteca.agregar_libro(libro2)
# Mostrar el estado inicial de la biblioteca
mi_biblioteca.mostrar_libros()
# Prestar un libro
mi_biblioteca.prestar_libro("Cien Años de Soledad")
mi_biblioteca.prestar_libro("Cien Años de Soledad")
# Intentar prestar un libro sin copias
mi_biblioteca.prestar_libro("Cien Años de Soledad")
mi_biblioteca.prestar_libro("Cien Años de Soledad")
# Mostrar el estado después de prestar
mi_biblioteca.mostrar_libros()
# Devolver un libro
mi_biblioteca.devolver_libro("Cien Años de Soledad")
# Mostrar el estado final
mi_biblioteca.mostrar_libros()

"""Ejercicio 2: Sistema de Gestión de Alumno"""
# Importar las clases Alumno y Curso desde el módulo Clases_De_Alumno
from Ejercicio2.Clases_De_Alumno import Alumno, Curso
# Crear una instancia del curso
curso_poo = Curso("Programación Orientada a Objetos")
# Crear instancias de alumnos
alumno1 = Alumno("Ana Pérez")
alumno2 = Alumno("Luis Gómez")
alumno3 = Alumno("Sofía López")
# Inscribir alumnos en el curso
curso_poo.inscribir_alumno(alumno1)
curso_poo.inscribir_alumno(alumno2)
curso_poo.inscribir_alumno(alumno3)
# Listar alumnos inscritos
curso_poo.listar_alumnos()
# Remover un alumno
curso_poo.remover_alumno("Luis Gómez")
# Listar alumnos después de remover uno
curso_poo.listar_alumnos()
# Intentar remover un alumno que no está en el curso
curso_poo.remover_alumno("Pedro Rojas")
# Listar alumnos una última vez
curso_poo.listar_alumnos()

"""Ejercicio 3: Sistema de Gestión de Ítems"""
# Importar las clases Item y Pedido desde el módulo Clases_De_Ítem
from Ejercicio3.Clases_De_Ítem import Item, Pedido
# Crear una instancia del pedido
mi_pedido = Pedido()
# Crear instancias de ítems
item1 = Item("Laptop", 1200.00, 1)
item2 = Item("Mouse", 25.50, 2)
item3 = Item("Teclado mecánico", 80.00, 1)
# Agregar ítems al pedido
mi_pedido.agregar_item(item1)
mi_pedido.agregar_item(item2)
mi_pedido.agregar_item(item3)
# Mostrar el pedido completo y su total
mi_pedido.mostrar_pedido()

"""Ejercicio 4: Sistema de Gestión de Sensor"""
# Importar la clase Sensor desde el módulo clases_De_Sensor
from Ejercicio4.Clases_De_Sensor import Sensor
# Crear una instancia del sensor
sensor_temp = Sensor("Sensor de Temperatura")
# Registrar mediciones
sensor_temp.registrar_valor(22.5)
sensor_temp.registrar_valor(23.1)
sensor_temp.registrar_valor(21.9)
sensor_temp.registrar_valor(24.0)
# Obtener y mostrar las estadísticas
print("\n📊 Análisis de Mediciones:")
print(f"Sensor: {sensor_temp.nombre}")
print(f"Número de mediciones: {len(sensor_temp.mediciones)}")
print(f"Promedio de mediciones: {sensor_temp.obtener_promedio():.2f}°C")
print(f"Valor máximo: {sensor_temp.obtener_maximo()}°C")
print(f"Valor mínimo: {sensor_temp.obtener_minimo()}°C")

"""Ejercicio 5: Sistema de Gestión de Películas"""
#Importar las clases Pelicula y Catalogo desde el módulo Clases_De_Película
from Ejercicio5.Clases_De_Película import Pelicula, Catalogo
# Crear una instancia del catálogo
mi_catalogo = Catalogo()
# Crear instancias de películas
p1 = Pelicula("La La Land", "Musical", 2016)
p2 = Pelicula("Gladiator", "Acción", 2000)
p3 = Pelicula("El Padrino", "Drama", 1972)
p4 = Pelicula("Mulan", "Acción", 2020)
# Agregar películas al catálogo
mi_catalogo.agregar_pelicula(p1)
mi_catalogo.agregar_pelicula(p2)
mi_catalogo.agregar_pelicula(p3)
mi_catalogo.agregar_pelicula(p4)
# Listar todas las películas
mi_catalogo.listar_todas()
# Buscar una película por título
mi_catalogo.buscar_por_titulo("gladiator")
# Filtrar películas por género
mi_catalogo.filtrar_por_genero("Acción")
mi_catalogo.filtrar_por_genero("Ciencia Ficción")

"""Ejercicio 6: Sistema de Gestión de Usuarios"""
# Importar las clases Usuario y Auth desde el módulo clases_De_Usuario
from Ejercicio6.Clases_De_Usuario import Usuario, Auth
# Crear una instancia del sistema de autenticación
sistema_auth = Auth()
# Intentar registrar un nuevo usuario
sistema_auth.registrar_usuario("admin", "12345")
sistema_auth.registrar_usuario("usuario1", "pass123")
# Intentar registrar un usuario que ya existe
sistema_auth.registrar_usuario("admin", "nueva_pass")
# Intentar iniciar sesión con credenciales correctas
sistema_auth.login("admin", "12345")
# Intentar iniciar sesión con contraseña incorrecta
sistema_auth.login("admin", "password_incorrecta")
# Intentar iniciar sesión con un usuario que no existe
sistema_auth.login("usuario_inexistente", "cualquier_pass")

"""Ejercicio 7: Sistema de Gestión de Contactos"""
# Importar las clases Contacto y Agenda desde el módulo Clases_De_Contacto
from Ejercicio7.Clases_De_Contacto import Contacto, Agenda
# Crear una instancia de la agenda
mi_agenda = Agenda()
# Crear instancias de contactos
c1 = Contacto("Juan Pérez", "912345678", "juan.perez@email.com")
c2 = Contacto("María Gómez", "987654321", "maria.gomez@email.com")
c3 = Contacto("Carlos Ruiz", "955554444", "carlos.ruiz@email.com")
# Agregar contactos a la agenda
mi_agenda.agregar_contacto(c1)
mi_agenda.agregar_contacto(c2)
mi_agenda.agregar_contacto(c3)
# Listar todos los contactos
mi_agenda.listar_contactos()
# Buscar un contacto
mi_agenda.buscar_contacto("María Gómez")
# Eliminar un contacto
mi_agenda.eliminar_contacto("Carlos Ruiz")
# Listar contactos después de la eliminación
mi_agenda.listar_contactos()
# Intentar eliminar un contacto que no existe
mi_agenda.eliminar_contacto("Pedro")

"""Ejercicio 8: Sistema de Gestión de Restaurante"""
# Importar las clases Mesa y Restaurante desde el módulo Clases_De_Mesa
from Ejercicio8.Clases_De_Mesa import Mesa, Restaurante
# Crear una instancia del restaurante
mi_restaurante = Restaurante()
# Agregar mesas al restaurante
mi_restaurante.agregar_mesa(Mesa(1, 2))
mi_restaurante.agregar_mesa(Mesa(2, 4))
mi_restaurante.agregar_mesa(Mesa(3, 2))
mi_restaurante.agregar_mesa(Mesa(4, 8))
# Mostrar el estado inicial
mi_restaurante.mostrar_estado_mesas()
# Realizar reservas
mi_restaurante.reservar_mesa(4)
mi_restaurante.reservar_mesa(2)
mi_restaurante.reservar_mesa(3)
# Mostrar el estado después de las reservas
mi_restaurante.mostrar_estado_mesas()
# Liberar una mesa
mi_restaurante.liberar_mesa(2)
# Mostrar el estado final
mi_restaurante.mostrar_estado_mesas()

"""Ejercicio 9: Sistema de Gestión de Productos"""
# Importar las clases Producto y Carrito desde el módulo Clases_De_Producto
from Ejercicio9.Clases_De_Producto import Producto, Carrito
# Crear productos
p1 = Producto("Monitor", 250.00)
p2 = Producto("Teclado", 75.00)
p3 = Producto("Ratón", 30.50)
# Crear un carrito de compras
mi_carrito = Carrito()
# Agregar productos al carrito
mi_carrito.agregar_producto(p1, 1)
mi_carrito.agregar_producto(p2, 2)
mi_carrito.agregar_producto(p3, 1)
# Calcular el total sin descuento
total_sin_descuento = mi_carrito.calcular_total()
print(f"\n🛒 Total del carrito sin descuento: ${total_sin_descuento:.2f}")
# Aplicar un descuento del 15%
total_con_descuento = mi_carrito.aplicar_descuento(15)
if total_con_descuento is not None:
    print(f"💰 Total del carrito con 15% de descuento: ${total_con_descuento:.2f}")
# Intentar aplicar un descuento inválido
mi_carrito.aplicar_descuento(120)

"""Ejercicio 10: Sistema de Gestión de Notas"""
# Importar las clases Nota y Estudiante desde el módulo Clases_De_Nota
from Ejercicio10.Clases_De_Nota import Nota, Estudiante
# Crear una instancia de Estudiante
estudiante1 = Estudiante("Sofía")
# Agregar notas al estudiante
estudiante1.agregar_nota("Programación", 6.5)
estudiante1.agregar_nota("Bases de Datos", 5.8)
estudiante1.agregar_nota("Redes", 7.0)
# Mostrar las calificaciones
estudiante1.mostrar_calificaciones()
# Calcular y mostrar el promedio
promedio = estudiante1.calcular_promedio()
print(f"\n📈 Promedio de notas de {estudiante1.nombre}: {promedio:.2f}")
# Crear un segundo estudiante sin notas
estudiante2 = Estudiante("Carlos")
estudiante2.mostrar_calificaciones()
print(f"📈 Promedio de notas de {estudiante2.nombre}: {estudiante2.calcular_promedio():.2f}")

"""Ejercicio 11: Sistema de Gestión de Empleados"""
# Importar las clases Empleado y Empresa desde el módulo Clases_De_Empleado
from Ejercicio11.Clases_De_Empleado import Empleado, Empresa
# Crear una instancia de Empresa
mi_empresa = Empresa()
# Crear instancias de Empleado
e1 = Empleado("Ana Torres", 1500.00)
e2 = Empleado("Pedro Soto", 2200.50)
e3 = Empleado("Carla Díaz", 1850.75)
# Contratar empleados
mi_empresa.contratar_empleado(e1)
mi_empresa.contratar_empleado(e2)
mi_empresa.contratar_empleado(e3)
# Listar empleados
mi_empresa.listar_empleados()
# Calcular y mostrar el gasto total
gasto = mi_empresa.calcular_gasto_total_sueldos()
print(f"\n💰 Gasto total en sueldos: ${gasto:,.2f}")

"""Ejercicio 12: Sistema de Gestión de Cuentas Bancarias"""
# Importar las clases Cuenta y Banco desde el módulo Clases_De_Cuenta
from Ejercicio12.Clases_De_Cuenta import Cuenta, Banco
# Crear una instancia de Banco
mi_banco = Banco()
# Abrir cuentas
mi_banco.abrir_cuenta("Juan Pérez", 1000.00)
mi_banco.abrir_cuenta("María Gómez", 500.00)
# Mostrar el estado inicial
mi_banco.mostrar_estado_cuentas()
# Realizar un depósito y un retiro
mi_banco.buscar_cuenta("Juan Pérez").depositar(200.00)
mi_banco.buscar_cuenta("María Gómez").retirar(100.00)
# Mostrar el estado después de las operaciones
mi_banco.mostrar_estado_cuentas()
# Realizar una transferencia
mi_banco.transferir("Juan Pérez", "María Gómez", 150.00)
# Mostrar el estado final
mi_banco.mostrar_estado_cuentas()

"""Ejercicio 13: Sistema de Gestión de Mascotas"""
# Importar las clases Mascota y Veterinaria desde el módulo Clases_De_Mascota
from Ejercicio13.Clases_De_Mascota import Mascota, Veterinaria
# Crear una instancia de la veterinaria
mi_veterinaria = Veterinaria()
# Crear instancias de mascotas
m1 = Mascota("Max", "Perro", 5)
m2 = Mascota("Milo", "Gato", 2)
m3 = Mascota("Boby", "Perro", 8)
# Registrar mascotas
mi_veterinaria.registrar_mascota(m1)
mi_veterinaria.registrar_mascota(m2)
mi_veterinaria.registrar_mascota(m3)
# Listar todas las mascotas
mi_veterinaria.listar_mascotas()
# Buscar una mascota por nombre
mi_veterinaria.buscar_mascota("Milo")
mi_veterinaria.buscar_mascota("Firulais")
# Calcular y mostrar la edad promedio
promedio_edad = mi_veterinaria.calcular_edad_promedio()
print(f"\n📈 La edad promedio de las mascotas es: {promedio_edad:.2f} años")

"""Ejercicio 14: Sistema de Gestión de Preguntas de Examen"""
# Importar las clases Pregunta y Examen desde el módulo Clases_De_Pregunta
from Ejercicio14.Clases_De_Pregunta import Pregunta, Examen
# Crear una instancia del examen
examen_poo = Examen()
# Crear instancias de preguntas
p1 = Pregunta("¿Qué es un objeto en POO?", "Una instancia de una clase.")
p2 = Pregunta("¿Qué es un método?", "Una función dentro de una clase.")
p3 = Pregunta("¿Qué es la herencia?", "Capacidad de una clase de derivar atributos y métodos de otra.")
# Agregar preguntas al examen
examen_poo.agregar_pregunta(p1)
examen_poo.agregar_pregunta(p2)
examen_poo.agregar_pregunta(p3)
# Listar las preguntas del examen
examen_poo.listar_preguntas()
# Contar el total de preguntas
total = examen_poo.contar_preguntas()
print(f"\n📊 El examen tiene un total de {total} preguntas.")