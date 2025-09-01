#__Main__

#__ejercicio_1:


# from ejercicio1.clases.biblioteca import Biblioteca
# from ejercicio1.clases.libro import Libro

# libro1 = Libro("1984","George Orwell",0)
# libro2 = Libro("la metamorfosis","Franz Kafka",0)
# libro3 = Libro("el principito","Antoine de Saint-Exupéry",0)


# mi_biblioteca = Biblioteca()

# mi_biblioteca.agregar_libro(libro1)
# mi_biblioteca.agregar_libro(libro1)
# mi_biblioteca.agregar_libro(libro1)
# mi_biblioteca.agregar_libro(libro2)


# mi_biblioteca.mostrar_lista_libros()


# mi_biblioteca.presta_libro(libro2)


# mi_biblioteca.devolver_libro(libro2)


# mi_biblioteca.mostrar_lista_libros()






#__ejercicio_2

# from ejercicio2.clases.alumno import Alumno
# from ejercicio2.clases.curso import Curso


# curso1 = Curso("8-A")


# alumno1 = Alumno("Manuel Gustavo","Abarca Reyes")
# alumno2 = Alumno("Arturo Patricio","Gonzalez Mendez")
# alumno3 = Alumno("Luis Mauricio","Parra Jorquera")
# alumno4 = Alumno("Luis Ignacio","Urra Vergara")



# curso1.inscribir_alumno(alumno1)    
# curso1.inscribir_alumno(alumno2)
# curso1.inscribir_alumno(alumno3)
# curso1.inscribir_alumno(alumno4)


# curso1.listado_alumnos()

# curso1.quitar_alumno()






#__ejercicio_3

# from ejercicio3.clases.item import Item
# from ejercicio3.clases.pedido import Pedido


# mi_pedido = Pedido()


# item1 = Item("globos",30,50)
# item2 = Item("vasos plásticos",100,40)

# producto1 = item1.nombre
# precio1 = item1.precio
# cantidad1 = item1.cantidad

# item1 = Item(producto1,precio1,cantidad1)



# producto2 = item2.nombre
# precio2 = item2.precio
# cantidad2 = item2.cantidad


# item2= Item(producto2,precio2,cantidad2)


# mi_pedido.agregar_item(item1)
# mi_pedido.agregar_item(item2)



# mi_pedido.detalle_pedido()

# print("El total del pedido es: $",mi_pedido.calculo_total())









#__ejercicio_4


from ejercicio4.clases.sensor import Sensor


sensor_vibraciones = Sensor("sensor_vibraciones")


sensor_vibraciones.registrar_valores()
sensor_vibraciones.registrar_valores()
sensor_vibraciones.registrar_valores()



print(sensor_vibraciones.lista_mediciones)


sensor_vibraciones.promedio()























