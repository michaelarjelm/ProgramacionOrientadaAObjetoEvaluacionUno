# ~ Creamos la clase Producto y Carrito
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.productos = {} # ~ Diccionario para almacenar los productos

    def agregarProducto(self, producto: Producto, cantidad: int):
        if producto.nombre in self.productos: # ~ Si ya existia el producto, actualizamos la cantidad
            self.productos[producto.nombre]['cantidad']+= cantidad
            print(f"Cantidad de '{producto.nombre}' actualizada!")
        else: # ~ Si no existia el producto, lo agregamos
            self.productos[producto.nombre] = {'producto': producto, 'cantidad': cantidad}
            print(f"Se ha agregado '{producto.nombre}' al carrito.")

    def calcularTotal(self, descuento=0):
        subtotal = 0 # ~ Inicializamos el subtotal en 0 
        for producto in self.productos.values(): # ~ Recorremos los productos en el carrito, con 'values' obtenemos los valores del diccionario
            subtotal += producto['producto'].precio * producto['cantidad'] # ~ Calculamos el subtotal

        total = subtotal - (subtotal * descuento / 100) # ~ Aplicamos el descuento si lo hay
        return total # ~ Retornamos el total
    
    
