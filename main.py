from ejercicio1.ejercicio1 import Biblioteca
from ejercicio11.ejercicio11 import Empleado
from ejercicio2.ejercicio2 import Alumno
from ejercicio3.ejercicio3 import Item
from ejercicio4.ejercicio4 import Sensor
from ejercicio5.ejercicio5 import Pelicula
from ejercicio6.ejercicio6 import Usuario
from ejercicio7.ejercicio7 import Contacto
from ejercicio8.ejercicio8 import Mesa
from ejercicio9.ejercicio9 import Producto

#Ejercicio1
print("Ejercicio1")

biblio = Biblioteca("harry potter","harry potter","papelucho")
print(biblio.mostrar())
#Ejercicio2
print("")
print("Ejercicio2")
curso = Alumno("benjamin","pedro")
#Ejercicio3
print("")
print("Ejercicio3")
total = Item(1500,3)
#Ejercicio4
print("")
print("Ejercicio4")
pedido = Sensor("sensor de proximidad",6000)
#Ejercicio5
print("")
print("Ejercicio5")
peli = Pelicula("los increibles","dibujo animado",2002)
#Ejercicio6
print("")
print("Ejercicio6")
user = Usuario("camilo","camilo123")
#Ejercicio7
print("")
print("Ejercicio7")
contactos = Contacto ("camilo",12345678,"hola@gmail.com")
#Ejercicio8
print("")
print("Ejercicio8")
mesas = Mesa(1,6,"libre")
#Ejercicio9
print("")
print("Ejercicio9")
carrito = Producto("manjarate",1000,4,30)
#Ejercicio10
print("")
print("Ejercicio10")
empresa = Empleado("pedro",800000)