# Ejercicio 1: Libro y Biblioteca
from ejercicio1.Libro import Libro
from ejercicio1.Biblioteca import Biblioteca

print("Ejercicio 1: Libro y Biblioteca")
biblio = Biblioteca()
for _ in range(2): #para agregar 2 libros como ejemplo
    titulo = input("Ingrese título del libro: ")
    autor = input("Ingrese autor del libro: ")
    copias = input("Ingrese número de copias: ") 
    libros = Libro(titulo, autor, copias)
biblio.agregar_libro(libros)
biblio.mostrar_listado() # no se pq no se muestran
titulo_prestar = input("Ingrese título del libro a prestar: ")
biblio.prestar(titulo_prestar)
titulo_devolver = input("Ingrese título del libro a devolver: ")
biblio.devolver(titulo_devolver)
biblio.mostrar_listado() #no se porque no se me muestran
print("\n")

# Ejercicio 2: Alumno y Curso
from ejercicio2.Alumno import Alumno
from ejercicio2.Curso import Curso

print("Ejercicio 2: Alumno y Curso")
nombre_curso = input("Ingrese nombre del curso: ")
curso = Curso(nombre_curso)
for _ in range(2):  # Inscribir 2 alumnos como ejemplo
    nombre_alumno = input("Ingrese nombre del alumno a inscribir: ")
    alumno = Alumno(nombre_alumno)
    curso.inscribir(alumno)
curso.listar_alumnos()
nombre_remover = input("Ingrese nombre del alumno a remover: ")
curso.remover(nombre_remover)
curso.listar_alumnos()
print("\n")

# Ejercicio 3: Pedido e Item
from ejercicio3.Item import Item
from ejercicio3.Pedido import Pedido

print("Ejercicio 3: Pedido e Item")
pedido = Pedido()
for _ in range(2):  # Agregar 2 ítems como ejemplo
    nombre_item = input("Ingrese nombre del ítem: ")
    precio_item = input("Ingrese precio del ítem: ")
    cantidad_item = input("Ingrese cantidad del ítem: ")
    item = Item(nombre_item, precio_item, cantidad_item)
    pedido.agregar_item(item)
print(f"Total: {pedido.calcular_total()}")
print("\n")

# Ejercicio 4: Sensor y Mediciones
from ejercicio4.MedicionesySensor import Sensor

print("Ejercicio 4: Sensor y Mediciones")
nombre_sensor = input("Ingrese nombre del sensor: ")
sensor = Sensor(nombre_sensor)
num_mediciones = int(input("Ingrese cuántas mediciones desea registrar: "))
for i in range(num_mediciones): #i es donde se establece la cantidad de mediciones
    valor = input(f"Ingrese valor de medición {i+1}: ")
    sensor.registrar_valor(valor)
print(f"Promedio: {sensor.obtener_promedio()}")
print(f"Máximo: {sensor.obtener_maximo()}")
print(f"Mínimo: {sensor.obtener_minimo()}") #f es para formatear cadenas y establecer variables lo vi en un video y ejemplos de IAs
print("\n")

# Ejercicio 5: Película y Catálogo
from ejercicio5.Pelicula import Pelicula
from ejercicio5.Catalogo import Catalogo

print("Ejercicio 5: Película y Catálogo")
catalogo = Catalogo()
for _ in range(2):  # Agregar 2 películas como ejemplo
    titulo_pelicula = input("Ingrese título de la película: ")
    genero_pelicula = input("Ingrese género de la película: ")
    ano_pelicula = input("Ingrese año de la película: ")
    pelicula = Pelicula(titulo_pelicula, genero_pelicula, ano_pelicula)
    catalogo.agregar_pelicula(pelicula)
catalogo.listar_todas()
genero_filtro = input("Ingrese género para filtrar: ")
catalogo.filtrar_por_genero(genero_filtro)
titulo_buscar = input("Ingrese título para buscar: ")
catalogo.buscar_por_titulo(titulo_buscar)
print("\n")

# Ejercicio 6: Usuario y Autenticación simple
from ejercicio6.Usuario import Usuario 
from ejercicio6.Autenticacion import Aut 

print("Ejercicio 6: Usuario y Autenticación simple")
auth = Aut()
nombre = input("Ingrese nombre de usuario: ")
contraseña=input("Ingrese contraseña: ")
user = Usuario(nombre, contraseña)
auth.registrar_usuario(user)
login_nombre = input("Ingrese nombre de usuario para login: ")
login_contraseña=input("Ingrese contraseña para login: ")
if auth.login(login_nombre, login_contraseña):
    print("Login exitoso")
else:
    print("Login fallido")
print("\n")

# Ejercicio 7: Agenda y Contacto
from ejercicio7.Contacto import Contacto
from ejercicio7.Agenda import Agenda

print("Ejercicio 7: Agenda y Contacto")
agenda = Agenda()
for _ in range(2):  # Agregar 2 contactos como ejemplo
    nombre_contacto = input("Ingrese nombre del contacto: ")
    telefono_contacto = input("Ingrese teléfono del contacto: ")
    correo_contacto = input("Ingrese correo del contacto: ")
    contacto = Contacto(nombre_contacto, telefono_contacto, correo_contacto)
    agenda.agregar_contacto(contacto)
agenda.listar_contactos()
nombre_buscar = input("Ingrese nombre del contacto a buscar: ")
agenda.buscar_contacto(nombre_buscar)
nombre_eliminar = input("Ingrese nombre del contacto a eliminar: ")
agenda.eliminar_contacto(nombre_eliminar)
agenda.listar_contactos()
print("\n")

# Ejercicio 8: Restaurante, Mesa y Reserva
from ejercicio8.Mesa import Mesa
from ejercicio8.ReservayRestaurante import Restaurante #juntos por que no pude hacer que el codigo funcionara separados

print("Ejercicio 8: Restaurante, Mesa y Reserva")
restaurante = Restaurante()
for _ in range(2):  # Agregar 2 mesas como ejemplo
    numero_mesa = input("Ingrese número de la mesa: ")
    capacidad_mesa = input("Ingrese capacidad de la mesa: ")
    mesa = Mesa(numero_mesa, capacidad_mesa)
    restaurante.agregar_mesa(mesa)
restaurante.mostrar_estado_mesas()
numero_reservar = int(input("Ingrese número de mesa a reservar: "))
restaurante.reservar(numero_reservar)
numero_liberar = int(input("Ingrese número de mesa a liberar: "))
restaurante.liberar(numero_liberar)
restaurante.mostrar_estado_mesas()
print("\n")

# Ejercicio 9: Carrito con Descuento
from ejercicio9.Producto import Producto
from ejercicio9.Carrito import Carrito

print("Ejercicio 9: Carrito con Descuento")
carrito = Carrito()
for _ in range(2):  # Agregar 2 productos como ejemplo
    nombre_producto = input("Ingrese nombre del producto: ")
    precio_producto = input("Ingrese precio del producto: ")
    cantidad_producto = input("Ingrese cantidad del producto: ")
    producto = Producto(nombre_producto, precio_producto)
    carrito.agregar_producto(producto, cantidad_producto)
print(f"Total sin descuento: {carrito.calcular_total()}")
descuento = input("Ingrese porcentaje de descuento: ")
carrito.aplicar_descuento(descuento)
print(f"Total con descuento: {carrito.calcular_total()}")
print("\n")

# Ejercicio 10: Estudiante y Nota
from ejercicio10.Nota import Nota
from ejercicio10.Estudiante import Estudiante

print("Ejercicio 10: Estudiante y Nota")
nombre_estudiante = input("Ingrese nombre del estudiante: ")
estudiante = Estudiante(nombre_estudiante)
for _ in range(2):  # Agregar 2 notas como ejemplo
    asignatura = input("Ingrese asignatura: ")
    calificacion = input("Ingrese calificación: ")
    nota = Nota(asignatura, calificacion)
    estudiante.anadir_nota(nota)
estudiante.mostrar_calificaciones()
print(f"Promedio: {estudiante.calcular_promedio()}")
print("\n")

# Ejercicio 11: Empleado y Empresa
from ejercicio11.Empleado import Empleado
from ejercicio11.Empresa import Empresa

print("Ejercicio 11: Empleado y Empresa")
empresa = Empresa()
for _ in range(2):  # Contratar 2 empleados como ejemplo
    nombre_empleado = input("Ingrese nombre del empleado: ")
    sueldo_empleado = input("Ingrese sueldo del empleado: ")
    empleado = Empleado(nombre_empleado, sueldo_empleado)
    empresa.contratar_empleado(empleado)
empresa.listar_empleados()
print(f"Gasto total en sueldos: {empresa.calcular_gasto_total()}")
print("\n")

# Ejercicio 12: Banco y Cuentas
from ejercicio12.Cuenta import Cuenta
from ejercicio12.Banco import Banco

print("Ejercicio 12: Banco y Cuentas")
banco = Banco()
for _ in range(2):  # Abrir 2 cuentas como ejemplo
    titular_cuenta = input("Ingrese titular de la cuenta: ")
    saldo_cuenta = input("Ingrese saldo inicial: ")
    cuenta = Cuenta(titular_cuenta, saldo_cuenta)
    banco.abrir_cuenta(cuenta)
banco.mostrar_estado_cuentas()
titular_origen = input("Ingrese titular de cuenta origen: ")
titular_destino = input("Ingrese titular de cuenta destino: ")
monto_transferir = input("Ingrese monto a transferir: ")
banco.transferir_dinero(titular_origen, titular_destino, monto_transferir)
banco.mostrar_estado_cuentas()
print("\n")

# Ejercicio 13: Veterinaria y Mascotas
from ejercicio13.Mascota import Mascota
from ejercicio13.Veterinaria import Veterinaria

print("Ejercicio 13: Veterinaria y Mascotas")
veterinaria = Veterinaria()
for _ in range(2):  # Registrar 2 mascotas como ejemplo
    nombre_mascota = input("Ingrese nombre de la mascota: ")
    especie_mascota = input("Ingrese especie de la mascota: ")
    edad_mascota = input("Ingrese edad de la mascota: ")
    mascota = Mascota(nombre_mascota, especie_mascota, edad_mascota)
    veterinaria.registrar_mascota(mascota)
veterinaria.listar_mascotas()
nombre_buscar = input("Ingrese nombre de la mascota a buscar: ")
veterinaria.buscar_por_nombre(nombre_buscar)
print(f"Edad promedio: {veterinaria.calcular_edad_promedio()}")
print("\n")

# Ejercicio 14: Examen y Preguntas
from ejercicio14.Pregunta import Pregunta
from ejercicio14.Examen import Examen

print("Ejercicio 14: Examen y Preguntas")
examen = Examen()
for _ in range(2):  # Agregar 2 preguntas como ejemplo
    enunciado = input("Ingrese enunciado de la pregunta: ")
    respuesta = input("Ingrese respuesta correcta: ")
    pregunta = Pregunta(enunciado, respuesta)
    examen.anadir_pregunta(pregunta)
examen.listar_preguntas()
print(f"Total de preguntas: {examen.contar_total_preguntas()}")
print("\n")
